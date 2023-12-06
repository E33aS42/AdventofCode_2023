#!/usr/bin/env python3
import numpy as np
import pandas as pd
import re

with open('input.txt') as f:
	lines = f.readlines()

# with open('ex.txt') as f:
# 	lines = f.readlines()

leny = len(lines)
lenx = len(lines[0])

nbmat = []
symbmat = []


for i in range(leny):
	numbers = re.findall('[0-9]+', lines[i])
	nbmat.append([])
	# test = "........*...48@.662.100...............590...*........#.566.....................15..../426.............774...............+...........*......."
	# test = ".339&.*74.........402.581............518&.......*....823.....874..102..678.74..............219....114..................836..915..245.-......"
	# ntest = re.findall('[0-9]+', test)
	# mtest = []
	# mtest.extend([{m.start(): m.group()} for m in re.finditer('[0-9]+', test)])
	# print(mtest)


	
	# get numbers indexes
	nbmat[i].extend([{m.start(): m.group()} for m in re.finditer('[0-9]+', lines[i])])
	dict_str = {}
	for j in nbmat[i]:
		dict_str |= j
	nbmat[i] = [dict_str]


	# find special characters indexes
	symbdict = {}
	k = 0
	for j in lines[i]:
		if j.isdigit() or j == '.' or j == '\n':
			k += 1
			continue
		symbdict[k] = j
		k += 1
	symbmat.append([symbdict])

	# if i == 0: break
# print(list(nbmat[0][0].items()))
# print(nbmat)
# print(symbmat)

listnb = []

for i in range(leny):
	for k, n in list(nbmat[i][0].items()):
		cn = 0
		# check current line
		ind_sym_line = set(symbmat[i][0].keys())
		if k - 1 in ind_sym_line or k + len(n) in ind_sym_line:
			listnb.append(int(n))
			cn = 1
			continue

		# check line above
		if i < leny - 1:
			ind_sym_above = set(symbmat[i + 1][0].keys())
			for p in range(k - 1, k + len(n) + 2):
				if p in ind_sym_above:
					listnb.append(int(n))
					cn = 1
					break

		# check line below
		if i > 0 and cn == 0:		
			ind_sym_below = set(symbmat[i - 1][0].keys())
			for p in range(k - 1, k + len(n) + 2):
				if p in ind_sym_below:
					listnb.append(int(n))
					cn = 1
					break


	# if i == 1: break

print(listnb)
print(sum(listnb))