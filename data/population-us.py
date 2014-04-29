#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import re 

print("""
DROP TABLE IF EXISTS population;
CREATE TABLE population (
	cc char(2) not null,
	year int unsigned not null,
	total int unsigned not null,
	factor1900 real not null
);
CREATE INDEX idx_pop ON population (cc,year);
""")

# '123,456' -> 123456
def numstr_uncomma(str):
	return int(''.join(re.split(',', str)))

print('BEGIN TRANSACTION;')

# popclockest.txt does 1900-1999
# NST_EST2009_ALLDATA.csv covers 2000-2009, here it is:
Pop = [
	(2009, 307006550),
	(2008 ,304374846),
	(2007, 301579895),
	(2006, 298593212),
	(2005, 295753151),
	(2004, 293045739),
	(2003, 290326418),
	(2002, 287803914),
	(2001, 285081556),
	(2000, 282171957),
]

for line in open('popclockest.txt', 'r').readlines():
	r = re.match('^July 1, (\d{4})\s+([0-9,]+)', line.strip())
	if r:
		year, p = r.groups()
		pop = numstr_uncomma(p)
		Pop.append((int(year), pop))

Baseline = float(Pop[-1][1])

for (year, pop) in Pop:
	print(("INSERT INTO population VALUES('us',%d,%d,%.5f);" \
		% (year, pop, Baseline / pop)))
print('COMMIT;')

