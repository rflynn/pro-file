#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
small script to highlight countries in svg map by CC 
"""

import xml.etree.ElementTree as ET

def fill(infile, outfile, paths):
	tree = ET.ElementTree()
	root = tree.parse(open(infile))
	#print(root)
	# FIXME: i want find("/path[@id='foo']") but this piece of shit doesn't support it
	# FIXME: not sure why it requires namespace... but it does.
	for p in root.findall('{http://www.w3.org/2000/svg}path'):
		id = p.get('id')
		if id in paths:
			p.set('style', 'fill:' + paths[id])
			#print('set %s ' % (id))
	#text = ET.tostring(root)
	#print(text)
	tree.write(outfile)

def highlight_countries(ccs, rgb='#000', infile='map/world-small.svg', outfile='map/world-small-out.svg'):
	fill(infile, outfile, dict(list(zip(ccs, [rgb] * len(ccs)))))

if __name__ == '__main__':
	highlight_countries('us ca mx br cn ru jp uk ie nl se no fr de es pt pl ro gr cz il eg in pk lk au mm th kh la'.split(' '))

