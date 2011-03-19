#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Surname reporting.  Consolidate surname database table data.
"""

import sqlite3
import names

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

import sys

def test():
	with sqlite3.connect('./names.db') as conn:
		for name in sys.argv[1:] + 'Non-existent Smith Nguyen Washington'.split(' '):
			norm = names.normalize(name)
			e = ethnicity(conn, norm)
			o = origin(conn, norm)
			print('%-15s %5.2f%% %-6s %s' % (name,e[1],e[0],' '.join(o)))

if __name__ == '__main__':
	test()

