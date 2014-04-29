#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

"""
Goal: based on historical life expectancy, calculate the odds that someone
born in a certain year is still alive today

Called a LIFE TABLE

Since we're only interested in people who are currently alive, this allows
us to adjust historical name/birth probabilities towards younger, more-likely-alive people
"""

# Odds you will still be alive at a certain age in 2006
# Source: National Vital Statistics Reports, Vol. 58, No. 21, June 28, 2010 p. 7-8 "Table 1. Life table for the total population: United States, 2006" http://www.cdc.gov/nchs/data/nvsr/nvsr58/nvsr58_21.pdf [Accessed March 10 2011]
# 
LT2006 = (
	1.0000, # 0-1 years old
	.99329, .99285, .99255, .99233, .99216, .99199, .99184, .99169, .99157, .99147,
	.99138, .99130, .99117, .99097, .99065, .99022, .98967, .98902, .98828, .98747,
	.98658, .98561, .98459, .98355, .98253, .98153, .98055, .97957, .97859, .97759,
	.97657, .97552, .97444, .97331, .97213, .97089, .96958, .96816, .96663, .96495,
	.96311, .96111, .95893, .95655, .95397, .95116, .94812, .94485, .94132, .93750,
	.93337, .92891, .92411, .91898, .91352, .90773, .90160, .89507, .88810, .88057,
	.87240, .86350, .85385, .84350, .83251, .82086, .80855, .79548, .78154, .76661,
	.75059, .73339, .71485, .69485, .67331, .65016, .62544, .59915, .57132, .54201,
	.51132, .47938, .44637, .41250, .37805, .34332, .30865, .27444, .24108, .20898,
	.17854, .15012, .12406, .10059, .07991, .06207, .04706, .03475, .02494, .01737,
	.0 # 100-101 years old
)

print("""
DROP TABLE IF EXISTS life_table_us;
CREATE TABLE life_table_us (
	year INT UNSIGNED NOT NULL,
	prob REAL NOT NULL
);
CREATE INDEX idx_life_table_us_year ON life_table_us (year);
BEGIN TRANSACTION;
""")

import time
CurrentYear = time.localtime().tm_year

for year in range(1900, CurrentYear+1):
	ago = CurrentYear - year
	ago = min(len(LT2006)-1, ago)
	prob = LT2006[ago]
	print(('INSERT INTO life_table_us VALUES (%d, %.5f);' % (year, prob)))

print('COMMIT;')

