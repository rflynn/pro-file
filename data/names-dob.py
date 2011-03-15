#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generate HTML/png name popularity report over time by integrating statistics.
"""

import math, cairo
from itertools import dropwhile, takewhile

# 
def meanval(l):
	return float(sum(l)) / max(1, len(l))

# 
def meani(l):
	s = sum(l)
	mean = float(s) / 2
	for i in range(0, len(l)-1):
		if l[i] >= mean:
			return i
		mean -= l[i]
	return 0

def variance(l):
	m = meanval(l)
	v = float(sum([(n-m)**2 for n in l])) / len(l)
	return v

def stddev(l):
	return math.sqrt(variance(l))

# determine the smallest range of years that totals a certain pct of the total
def range_pct(l, pct):
	s = float(sum(l))
	sp = s * pct
	lo = 0
	hi = len(l)-1
	curr = s
	while lo < hi and curr > sp:
		if l[lo] <= l[hi]:
			if curr - l[lo] > sp:
				lo += 1
				curr -= l[lo]
			else:
				break
		else:
			if curr - l[hi] > sp:
				hi -= 1
				curr -= l[hi]
			else:
				break
	return (lo, hi)

# determine the most likely range of 'years', and how likely it is
def range_years(l, years):
	lo = 0
	hi = len(l)-1
	while hi - lo > years:
		if l[lo] <= l[hi]:
			lo += 1
		else:
			hi -= 1
	total = float(sum(l))
	if total == 0:
		total = 1
	rtotal = sum(l[lo:hi+1])
	return ((lo, hi), rtotal / total * 100.)

# generate a barchart image file
def graph(name, p, Width=110, Height=50, BarWidthPx=2, BarSpacePx=1):
	try:
		XScale=BarWidthPx + BarSpacePx
		# p is [(year,fcnt)]
		Width *= XScale
		surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, Width, Height)
		cr = cairo.Context(surface)
		cr.set_source_rgba(0,0,0,1)
		cr.select_font_face('Verdana')
        	cr.set_font_size(8.0)
		cnts = [cnt for year,cnt in p]
		mi = meani(cnts)
		mval = cnts[mi]
		sd = stddev(cnts)
		(mloi,mhii),pct = range_years(cnts, 30)
		# graph individual years
		for i,(year,fcnt) in enumerate(p):
			cr.set_source_rgba(0,0,0,.3)
			x = (year - 1900) * XScale
			h = max(1, fcnt / 1000)
			if i >= mloi and i <= mhii:
				cr.set_source_rgba(0,0,0,1)
			if i == mi:
				cr.set_source_rgba(1,0,0,1)
				w, = cr.text_extents(str(year))[2:3]
                		cr.move_to(max(0, x-w/2.), Height)
                		cr.show_text(str(year))
                		cr.stroke()
			cr.rectangle(x, Height-h-7, BarWidthPx, h)
			cr.fill()
			cr.stroke()
		# graph 80% 
		cr.set_source_rgba(1,0,0,0.6)
		mloi,mhii = range_pct(cnts, 0.80)
		pctrng = mhii - mloi
		cr.rectangle(mloi * XScale, Height-7, pctrng * XScale, 1)
		cr.fill()
		cr.stroke()
		# write file
		surface.write_to_png('name-dob-chart/' + name + '.png')
		surface.finish()
		return (pct, pctrng)
	except:
		sys.stderr.write("Unexpected error:%s\n" % (sys.exc_info()[0]))
		raise
	return (0,0)

import sys
import sqlite3
import time 

CurrentYear = time.localtime().tm_year

def name_birth_totals(conn, name):
	c = conn.cursor()
	c.execute("""
	select	n.year,
		sum(n.total * p.factor1900 * lt.prob) as fcnt
	from givenname_birthyear n
	join population p on p.cc = n.cc and p.year = n.year
       	join life_table_us lt on lt.year = n.year
	where name=? and n.cc=?
	group by name, n.year
	order by n.year asc""", (name,'us'))
	rows = c.fetchall()
	c.close()
	d = dict(rows)
	# fill in gap years with zero, simplifies graphing
	fill = [(y, d[y] if y in d else 0.)
			for y in range(1900, CurrentYear+1)]
	return fill

conn = sqlite3.connect('./names.db')

print("<html><body>")
sys.stderr.write('top names...\n')
c = conn.cursor()
c.execute("""
select name,
       sum(n.total * p.factor1900) as fcnt
       -- calculate the probability of the birth year of someone alive today
       -- n.total is the total number of name-births
       -- p.factor1900 normalizes name popularity based on u.s. population
       -- lt.prob takes into account human life expectancy at a given age
from givenname_birthyear n
join population p on p.cc = n.cc and p.year = n.year
join life_table_us lt on lt.year = n.year
where n.cc = 'us'
group by name
order by fcnt desc
limit 1000
""")
for name,_ in c:
	sys.stderr.write(name + ' ')
	(pct, pctrng) = graph(name, name_birth_totals(conn, name))
	print("""
<div style="display:inline-block">
	<div>%s <small>(%.1f%% &plusmn;15 yr) (&plusmn;%.1f yr @ 80%%)</small></div>
	<img src="name-dob-chart/%s.png">
</div>""" % (name, pct, pctrng / 2., name))
print("</body></html>")
sys.stderr.write('\n')

