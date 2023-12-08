#!/usr/bin/env python3
import re
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


def check_end(next):
	end = [w for w in next if w.endswith('Z')]
	# print(f'end = {end}')
	if len(end) == len(next):
		return 1
	return 0

def get_next(next, cnt, k, i):
	new = []
	# print(f"i, cnt={cnt}, next={next}")
	for n in next:
		if n.endswith('Z') and cnt[n] == 0:
			cnt[n] = i
			new.append(n)
		elif n.endswith('Z') and cnt[n]:
			new.append(n)
		else:
			# print("seq: ", sequences[n][k])
			new.append(sequences[n][k])
	return cnt, new

def loop(cnt, n, j):
	next = n
	i = 0
	while not check_end(next) and i < len(instructions):
		for inst in instructions:
			# print(f'j={j}')
			i += 1
			if inst == 'L':
				cnt, next = get_next(next, cnt, 0, i + j)
			elif inst == 'R':
				cnt, next = get_next(next, cnt, 1, i + j)
	

	return cnt, next

zero = [0 for _ in range(len(end))]
cnt = dict(zip(end, zero))
# print(cnt)

next = start
j = 0

# print(check_end(end))
while not check_end(next):
# 	print(f"j={j}")
	# print(f"j, cnt={cnt}, next={next}")
	cnt, next = loop(cnt, next, j)

	print(cnt, next)
	j += 1
	# if j == 2: break

print(*cnt.values())
print(math.lcm(*cnt.values()))