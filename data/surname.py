#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Surname reporting.  Consolidate surname database table data.
"""

import sqlite3

def ethnicity(conn, name, cc='us'):
	c = conn.cursor()
	c.execute("""
		select likely_eth,likely_pct
		from surname_ethnicity_us_2000
		where name=?
		""", (name,))
	eth = c.fetchone()
	if eth == None:
		eth = (None, 0)
	c.close()
	return eth

def origin(conn, name):
	c = conn.cursor()
	c.execute("""
		select hint
		from surname_origin
		where name=?
		""", (name,))
	hints = [x[0] for x in c.fetchall()]
	c.close()
	return hints

import names

def lookup(conn, surnames):
	for name in surnames:
		# handle hyphenated surnames
		for subname in name.split('-'):
			norm = names.normalize(subname)
			e = ethnicity(conn, norm)
			o = origin(conn, norm)
			print(('%-15s %5.2f%% %-6s %s' % (subname,e[1],e[0],' '.join(o))))

def test(conn):
	lookup(conn, 'Non-existent Smith Nguyen Washington Johnson-Johnsson Smithford'.split(' '))
	# hyphenated married names
	lookup(conn, 'Johnson-Johnsson'.split(' '))
	# name blending
	lookup(conn, 'Smithford'.split(' '))

if __name__ == '__main__':
	import sys
	with sqlite3.connect('./names.sqlite3') as conn:
		if sys.argv[1:] != []:
			lookup(conn, sys.argv[1:])
		else:
			test(conn)

