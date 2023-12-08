#!/usr/bin/env python3
import re
import math

content = open("ex2.txt").read().strip().split("\n\n")
instructions = content[0]
tmp = content[1].split("\n")

# print(instructions)

sequences = {}
for i in tmp:
	sequences[i.split(" = ")[0]] = i.split(" = ")[1].strip("()").split(", ")

# print(sequences)

start = [w for w in sequences.keys() if w.endswith('A')]
end = [w for w in sequences.keys() if w.endswith('Z')]

print(start, end)

def get_next(next, cnt, k, i):
	new = []
	print(f'next = {next}')
	for n in next:
		if n.endswith('Z') and cnt[n] == 0:
			cnt[n] = i
			new.append(n)
		else:
			new.append(sequences[n][k])
	return cnt, new


def directions(d, next, cnt, i):
	try:
		assert d in "LR", "unknown instruction"
		if d == 'L':
			return cnt, get_next(next, cnt, 0, i)
		elif d == 'R':
			return cnt, get_next(next, cnt, 1, i)
	except AssertionError as e:
		print(e)
		exit()

def loop(b, cnt):
	next = b
	i = 0
	while not check_end(next) and i < len(instructions):
		for j in instructions:
			i += 1
			cnt, next = directions(j, next, cnt, i)
	return cnt, next

def check_end(next):
	end = [w for w in next if w.endswith('Z')]
	if len(end) == len(next):
		return 1
	return 0

zero = [0 for _ in range(len(end))]
cnt = dict(zip(end, zero))
print(cnt)

next = start
j = 0
while not check_end(next):
	print(f"j={j}")
	cnt, next = loop(next, cnt)

	print(cnt, next)
	j += 1
	if j == 2: break

print(math.lcm(*cnt))