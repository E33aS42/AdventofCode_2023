#!/usr/bin/env python3
import numpy as np
import pandas as pd
import re

with open('input.txt') as f:
	lines = f.readlines()


leny = len(lines)
lenx = len(lines[0])

nbmat = []
symbmat = []


for i in range(leny):
	numbers = re.findall('[0-9]+', lines[i])
	nbmat.append([])
	# test = "........*...48@.662.100...............590...*........#.566.....................15..../426.............774...............+...........*......."

	# get numbers indexes
	for n in numbers:
		nbmat[i].extend([{m.start(): n} for m in re.finditer(n, lines[i])])
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




	# i += 1
	# if i == 2: break
print(nbmat)
print(symbmat)

for i in range(leny):
	# check current line
	
	# check line above
	if i < leny - 1: 
		
		pass

	# check line below
	if i > 0:		
		pass