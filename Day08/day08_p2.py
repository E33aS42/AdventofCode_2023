#!/usr/bin/env python3
import math

content = open("input.txt").read().strip().split("\n\n")
instructions = content[0]
tmp = content[1].split("\n")

# print(instructions)

sequences = {}
for i in tmp:
	sequences[i.split(" = ")[0]] = i.split(" = ")[1].strip("()").split(", ")

# print(sequences)

start = [w for w in sequences.keys() if w.endswith('A')]
end = [w for w in sequences.keys() if w.endswith('Z')]

# print(start, end)

def directions(d, k):
	try:
		assert d in "LR", "unknown instruction"
		assert k in sequences.keys(), "unknown direction"
		if d == 'L':
			return sequences[k][0]
		elif d == 'R':
			return sequences[k][1]
	except AssertionError as e:
		print(e)
		exit()

def loop(b):
	next = b
	i = 0
	while next != end and i < len(instructions):
		for j in instructions:
			next = directions(j, next)
			i += 1
	return i, next

cnt_list = {}

for st in start:
	cnt = 0

	next = st
	while next not in end:
		c, next = loop(next)
		cnt += c
		# print(cnt, next)

	cnt_list[next] = cnt
print("total steps counts for each ending: ", cnt_list)
print("global steps count: ", math.lcm(*cnt_list.values()))