#!/usr/bin/env python3
import numpy as np
import pandas as pd
import re

input = pd.read_csv('input.txt', header = None).values
nb = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

arr_nb = np.empty((1000, 1), dtype=int)
i = 0
for line in input:
	val = ""
	# for a in line[0]:
	# 	if a in nb:
	# 		val += a
	# 		break
	# for b in line[0][::-1]:
	# 	if b in nb:
	# 		val += b
	# 		break
	# arr_nb[i] = (int(val))
	# i += 1


	m_start = re.search(r"\d", line[0])
	m_end = re.search(r"\d", line[0][::-1])
	if m_start:
		val += m_start.group()
	if m_end:
		val += m_end.group()
	arr_nb[i] = (int(val))
	i += 1
	
print(sum(arr_nb))

dict_nb = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

numbers = list(dict_nb.keys())
arr_nb2 = np.empty((1000, 1), dtype=int)
i = 0
for line in input:
	# line = ["hmbfjdfnp989mfivefiverpzrjs"]
	ind_str = []
	str_str = []
	m_start = re.search(r"\d", line[0])
	m_end = re.search(r"\d", line[0][::-1])
	if m_start:
		ind_str.append({m_start.start(): int(m_start.group())})
	if m_end:
		ind_str.append({len(line[0]) - 1 - m_end.start(): int(m_end.group())})
	ind_str.extend([ind for ind in [{line[0].find(word, 0): dict_nb[word]} for word in numbers] if list(ind.keys())[0] != -1])
	str_str.extend([ind for ind in [{line[0].find(word, 0): word} for word in numbers] if list(ind.keys())[0] != -1])


	dict_str = {}
	for j in str_str:
		dict_str |= j

	values = list(dict_str.values())
	for v in values:
		ind_str.extend([{b.start(): dict_nb[v]} for b in re.finditer(v, line[0])])

	dict_str = {}
	for j in ind_str:
		dict_str |= j

	
	keys = list(dict_str.keys())

	min_keys = min(keys)
	max_keys = max(keys)
	val = str(dict_str[min_keys]) + str(dict_str[max_keys])

	arr_nb2[i] = (int(val))
	i += 1
	# break

print(sum(arr_nb2))