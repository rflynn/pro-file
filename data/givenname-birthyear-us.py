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

# TODO: consolidate following blocks, shared in other places, into utility functions

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

import glob, re
import names

def yob_generator():
	files = glob.glob('./' + dir + '/yob*.txt')
	for filename in files:
		year = re.search('yob(\d+)\.txt', filename).group(1)
		if int(year) >= 1900:
			for line in open(filename, 'r').readlines():
				(name,gender,total) = line.strip().split(",")
				norm = names.normalize(name)
				yield (year, norm, gender, total)

import sqlite3

with sqlite3.connect('./names.db') as conn:
	c = conn.cursor()
	c.executescript("""
DROP TABLE IF EXISTS givenname_birthyear;
CREATE TABLE givenname_birthyear (
	year int not null,
	name text not null,
	gender text not null,
	total int not null
);

-- ugly pragmas to speed large insertion
PRAGMA synchronous = OFF;
PRAGMA temp_store = MEMORY;
PRAGMA journal_mode = OFF;
""")
	print('-- inserting yob records...')
	c.executemany('INSERT INTO givenname_birthyear VALUES(?,?,?,?)', yob_generator())
	print('-- creating index...')
	c.executescript("""
CREATE INDEX idx_name ON givenname_birthyear (name);
PRAGMA synchronous = DEFAULT;
PRAGMA temp_store = NORMAL;""")
	c.close()

