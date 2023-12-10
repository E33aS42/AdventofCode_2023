#!/usr/bin/env python3
import pandas as pd
import numpy as np
import re

"""
The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

with open('input.txt') as f:
	lines = f.readlines()

with open('ex') as f:
	lines = f.readlines()

print(len(lines))
for i in range(len(lines)):
	ind = re.search('S', lines[i])
	if ind != None:
		start = [i, ind.span()[0]]
		break

print(start)

def p_vert(p, ip, iv):
	"""
	p: input pipe, only 7, F (top side) and J, L (bottom side) can connect and another vert. pipe
	ip: index of coming input pipe
	iv: index of vertical pipe
	"""
	if (ip[0] == iv[0] - 1 and ip[1] == iv[1]):
		return [iv[0] + 1, iv[1]]
	elif (ip[0] == iv[0] + 1 and ip[1] == iv[1]):
		return [iv[0] - 1, iv[1]]
	else:
		return -1
	
def p_horiz(p, ip, iv):
	"""
	p: input pipe, only 7, J (right side) and L, F (left side) can connect, and another horiz. pipe
	ip: index of coming input pipe
	iv: index of vertical pipe
	"""
	if (ip[0] == iv[0] and ip[1] == iv[1] + 1):
		return [iv[0], iv[1] - 1]
	elif (ip[0] == iv[0] and ip[1] == iv[1] - 1):
		return [iv[0], iv[1] + 1]
	else:
		return -1
	
def pL(ip, iv):
	if (ip[0] == iv[0] - 1 and ip[1] == iv[1]):
		return [iv[0] + 1, iv[1] + 1]
	elif (ip[0] == iv[0] and ip[1] == iv[1] + 1):
		return [iv[0] - 1, iv[1] - 1]
	else:
		return -1
	
def pJ(ip, iv):
	if (ip[0] == iv[0] - 1 and ip[1] == iv[1]):
		return [iv[0] + 1, iv[1] - 1]
	elif (ip[0] == iv[0] and ip[1] == iv[1] - 1):
		return [iv[0] - 1, iv[1] + 1]
	else:
		return -1
	
def p7(ip, iv):
	if (ip[0] == iv[0] - 1 and ip[1] == iv[1]):
		return [iv[0] - 1, iv[1] - 1]
	elif (ip[0] == iv[0] and ip[1] == iv[1] + 1):
		return [iv[0] + 1, iv[1] + 1]
	else:
		return -1
	
def pF(ip, iv):
	if (ip[0] == iv[0] - 1 and ip[1] == iv[1]):
		return [iv[0] - 1, iv[1] + 1]
	elif (ip[0] == iv[0] and ip[1] == iv[1] + 1):
		return [iv[0] + 1, iv[1] - 1]
	else:
		return -1
	
def pstart(s):
	next = []
	if lines[s[0] - 1][s[1]] in {'7', 'F', '|'}:
		next += [lines[s[0] - 1][s[1]]]
	if lines[s[0] + 1][s[1]] in {'J', 'L', '|'}:
		next += lines[s[0] + 1][s[1]]
	if lines[s[0]][s[1] - 1] in {'L', 'F', '-'}:
		next += lines[s[0]][s[1] - 1]
	if lines[s[0]][s[1] + 1] in {'J', '7', '-'}:
		next += lines[s[0]][s[1] + 1] 
	return next


start_tiles = pstart(start)

