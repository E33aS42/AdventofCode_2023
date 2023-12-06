#!/usr/bin/env python3
import numpy as np
import pandas as pd
import re

input = pd.read_csv('input.txt', header = None).values

# Part 1

total = 0
i = 0
for line in input:
	val = ""
	m_start = re.search(r"\d", line[0])
	m_end = re.search(r"\d", line[0][::-1])
	if m_start:
		val += m_start.group()
	if m_end:
		val += m_end.group()
	total += int(val)
	i += 1
	
print(total)


# Part 2

dict_nb = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

numbers = list(dict_nb.keys())
total = 0
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

	total += int(val)
	i += 1

print(total)