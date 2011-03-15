#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':

	url = 'http://www.census.gov/genealogy/names/dist.all.last'
	file = 'surname-us-dist.all.last.txt'

	import os, sys, urllib
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

	print("""
	DROP TABLE IF EXISTS surname;
	CREATE TABLE surname (
		cc TEXT not null,
		name varchar(64) not null unique,
		pop_fact_us real not null default 0
	);
	BEGIN TRANSACTION;
	""")
	
	import re 
	
	for line in open(file, 'r').readlines():
		if line[0] == ';':
			continue
		(surname,fact,facttotal,nth) = re.split('[ ]+', line.strip())
		print("INSERT OR IGNORE INTO surname VALUES('us','%s',%.3f);" % \
			 (surname.strip(), float(fact)))
	print('COMMIT;')

