#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
U.S. given name births by year from the Social Security Administration
Download, extract, parse and generate SQL
"""

import sys, os

url = 'http://www.ssa.gov/oact/babynames/names.zip'
i = url.rfind('/')
file = url[i+1:]
dir = 'givenname-birthyear-us'

if os.path.exists(file):
	print('-- %s exists' % (file))
else:
	import urllib
	def reporthook(a,b,c): 
    		print("% 3.1f%% of %d bytes\r" % \
			(min(100, float(a * b) / c * 100), c)),
    		sys.stdout.flush()
     	print('-- %s ->  %s' % (url, file))
     	urllib.urlretrieve(url, file, reporthook)

if os.path.exists(dir):
	print('-- %s exists' % (dir))
else:
	import subprocess
	print('/*')
	sys.stdout.flush()
	subprocess.call(['unzip', '-d', dir, file])
	print('*/')

print("""
DROP TABLE IF EXISTS givenname_birthyear;
CREATE TABLE givenname_birthyear (
	year int not null,
	name text not null,
	gender text not null,
	total int not null
);

PRAGMA synchronous = OFF;
PRAGMA temp_store = MEMORY;
PRAGMA journal_mode = OFF;
PRAGMA count_changes = OFF;

BEGIN DEFERRED TRANSACTION;
""")

import glob, re
import names
files = glob.glob('./' + dir + '/yob*.txt')
for filename in files:
	year = re.search('yob(\d+)\.txt', filename).group(1)
	print('-- ' + year)
	if int(year) >= 1900:
		for line in open(filename, 'r').readlines():
			(name,gender,total) = line.strip().split(",")
			norm = names.normalize(name)
			print("INSERT INTO givenname_birthyear VALUES" +
				"(%s,'%s','%s',%s);" % (year, norm, gender, total))
print("""
COMMIT;
CREATE INDEX idx_name ON givenname_birthyear (name);
PRAGMA synchronous = DEFAULT;
PRAGMA temp_store = NORMAL;
""")

