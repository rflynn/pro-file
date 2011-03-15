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
	cc text not null,
	name text not null,
	gender text not null,
	total int not null
);
CREATE INDEX idx_name ON givenname_birthyear (name,cc);
BEGIN TRANSACTION;
""")

import glob, re
files = glob.glob('./' + dir + '/yob*.txt')
for filename in files:
	year = re.search('yob(\d+)\.txt', filename).group(1)
	print('-- ' + year)
	for line in open(filename, 'r').readlines():
		(name,gender,total) = line.strip().split(",")
		print("INSERT OR IGNORE INTO givenname_birthyear VALUES" +
			"(%s,'us','%s','%s',%s);" % (year, name, gender, total))
print('COMMIT;')

