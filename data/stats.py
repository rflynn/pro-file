#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Python implementation of simple statistical functions

# calculate the mean value of list elements
def meanval(l):
	return sum(l) / max(1, len(l))

# calculate the index at which the value of list elements is most even on each side
def meani(l):
	mean = sum(l) / 2
	for i in range(0, len(l)):
		if l[i] >= mean:
			return i
		mean -= l[i]
	return len(l)-1 

def variance(l):
	m = meanval(l)
	v = sum([(n-m)**2 for n in l]) / max(1, len(l))
	return v

def stddev(l):
	return math.sqrt(variance(l))

# find the smallest slice of l whose sum >= sum(l)*pct
# note: inefficient
def range_pct(l, pct):
	sp = sum(l) * pct # find slice >= this
	for r in range(1, len(l)-1):
		# slice sums of length r
		s = [(i,sum(l[i:i+r])) for i in range(0, len(l)-r)]
		i,total = max(s, key=lambda x:x[1])
		if total >= sp:
			return (i,i+r)
	return (0, max(0, len(l)-1))

# given a list of numbers 'l' and a contiguous subset size 'size'
# determine the contiguous slice of 'l' with the highest value, and
# determine what percent of the total it contains
def range_size(l, size):
	if len(l) <= size:
		return ((0, max(0, len(l)-1)), 100)
	# Θ(n)
	sumpos = [(0, sum(l[:size]))]
	for i in range(0, len(l)-size):
		sumpos.append((i+1, sumpos[-1][1] - l[i] + l[i+size]))
	lo,rtotal = max(sumpos, key=lambda x:x[1])
	hi = lo + size
	pct = rtotal / max(1, sum(l))
	return ((lo, hi), pct * 100)

if __name__ == '__main__':

	def test_range_pct():
		Expect = (
			((0,0), ([], 0.0)),
			((0,0), ([], 1.0)),
			((0,0), ([1], 0.0)),
			((0,0), ([1], 1.0)),
			((0,1), ([1,1], 0.5)),
			((0,1), ([1,1], 0.99)),
			((1,2), ([1,2,1], 0.5)),
			((0,2), ([2,2,1], 0.8)),
			((0,2), ([2,2,1], 3/7.)),
			((0,2), ([2,2,0,3], 0.51)),
		)
		for expres,param in Expect:
			res = range_pct(*param)
			if expres != res:
				print('range_pct',param,' expected:',expres,'got:',res)

	def test_range_size():
		Expect = (
			(((0,0),100.),     ([], 0)),
			(((0,0),100.),     ([], 1)),
			(((2,3), 50.),     ([1,2,3], 1)),
			(((1,3),5/6.*100), ([1,2,3], 2)),
			(((0,2),5/6.*100), ([3,2,1], 2)),
			(((2,4),4/7.*100), ([3,0,2,2], 2)),
		)
		for expres,param in Expect:
			res = range_size(*param)
			if expres != res:
				print('range_size',param,' expected:',expres,'got:',res)

	def test():
		test_range_size()
		test_range_pct()
		print('Test complete.')

	test()
	
