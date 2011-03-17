#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

"""
Python implementation of simple statistical functions
"""

# 
def meanval(l):
	return float(sum(l)) / max(1, len(l))

# 
def meani(l):
	mean = float(sum(l)) / 2
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

# given a list of numbers 'l' determine the smallest range of
# years that totals a certain percentage 'pct' of the total
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

# given a list of numbers 'l' and a contiguous subset size 'size'
# determine the contiguous slice of 'l' with the highest value, and
# determine what percent of the total it contains
def range_size(l, size):
	lo = 0
	hi = len(l)-1
	# FIXME: this is overly-simplistic and inaccurate
	# use sum() over slices
	while hi - lo > size:
		if l[lo] <= l[hi]:
			lo += 1
		else:
			hi -= 1
	total = sum(l)
	rtotal = sum(l[lo:hi+1])
	pct = float(rtotal) / max(1, total)
	return ((lo, hi), pct * 100)

