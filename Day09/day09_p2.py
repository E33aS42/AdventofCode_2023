#!/usr/bin/env python3
import pandas as pd
import numpy as np
import re


input = pd.read_csv('input.txt', delimiter=' ', dtype=int, header = None).values
# input = pd.read_csv('ex', delimiter=' ', dtype=int, header = None).values


def calc(line):
	dif = []
	for i in range(len(line) - 1):
		dif.append(line[i + 1] - line[i])
	return dif

cnt = 0

for line in input:
	mat_dif = [list(line)]
	dif = calc(line)
	mat_dif.append(dif)
	while not all(v == 0 for v in dif):
		dif = calc(dif)
		mat_dif.append(dif)

	# insert 0 at the beginning
	mat_dif[len(mat_dif) - 1].insert(0, 0)

	for i in range(len(mat_dif) - 2, -1, -1):
		# print(f'i={i}, {mat_dif[i]}')
		mat_dif[i].insert(0, mat_dif[i][0] - mat_dif[i + 1][0])
		# print(f'i={i}, {mat_dif[i]}')
	cnt += mat_dif[0][0]

print("result:", cnt)
