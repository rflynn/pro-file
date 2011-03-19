#!/usr/bin/env python
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
		norm = names.normalize(name)
		e = ethnicity(conn, norm)
		o = origin(conn, norm)
		print('%-15s %5.2f%% %-6s %s' % (name,e[1],e[0],' '.join(o)))

def test(conn):
	lookup(conn, 'Non-existent Smith Nguyen Washington'.split(' '))

if __name__ == '__main__':
	import sys
	with sqlite3.connect('./names.db') as conn:
		if sys.argv[1:] != []:
			lookup(conn, sys.argv[1:])
		else:
			test(conn)

