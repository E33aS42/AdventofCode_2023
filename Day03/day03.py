#!/usr/bin/env python3
import numpy as np
import pandas as pd
import re

with open('input.txt') as f:
	lines = f.readlines()

print(lines[0])

leny = len(lines)
lenx = len(lines[0])
print(leny, lenx)

listmat_nb = []
symbmat = []
# symbols = '[@_!#$%^&*()<>?/\|}{~:]-+='
special_char = "{[!@#$%\^&*()-+?_=,<>\|/\"]}"
# special_char = "{[@#$%^&*()-+?_=,<>\|]}"
# special_char = re.compile('{[\!@#$%^&*()-+?_=,<>|/"]}') 
# regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
text = "........*...48@.662.100...............590...*........#.566.....................15..../426.............774...............+...........*......."
# print(regex.search(text))


for i in range(leny - 1):
	numbers = re.findall('[0-9]+', lines[i])
	listmat_nb.append([])
	test = "........*...48@.662.100...............590...*........#.566.....................15..../426.............774...............+...........*......."
	for s in special_char:
		# print(s)
		# sym = re.findall(s, test)
		sym = test.find(s)
		# print(sym)
		
	# symbols = re.findall(special_char, lines[i])
	# symbmat.append([])
	# print(symbols)
	# print(regex.search(lines[i+1]))
	for n in numbers:
		listmat_nb[i].extend([{m.start(): n} for m in re.finditer(n, lines[i])])
	print(numbers)
	dict_str = {}
	for j in listmat_nb[i]:
		dict_str |= j
	listmat_nb[i] = [dict_str]
	print(listmat_nb[i])

	# for n in symbols:

	# 	symbmat[i].extend([{m.start(): n} for m in re.finditer(n, lines[i])])
	# print(symbmat)

	if i < leny - 1: # check line above
		# {m.start(0):int(m.group(0)) for m in re.finditer("\d+", strs)}
		pass

	if i > 0:		# check line below
		pass


	i += 1
	break