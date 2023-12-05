#!/usr/bin/env python3
import numpy as np
import pandas as pd
import re

with open('input.txt') as f:
	lines = f.readlines()

def parse(s):
	# Card   1: 30 51 48 31 36 33 49 83 86 17 | 17 33 31 70 90 37 86 45 58 21 83 52 59 68 55 32 20 43 48 75 30 42 80 60 71
	card = s.split(": ")[1].split(" | ")
	win = card[0].split()
	nb = card[1].split()
	total = 0
	for n in nb:
		if n in win:
			if total == 0:
				total = 1
			else:
				total *= 2
	return total

final = 0
for line in lines:
	final += parse(line)

print(final)


def parse2(s):
	# Card   1: 30 51 48 31 36 33 49 83 86 17 | 17 33 31 70 90 37 86 45 58 21 83 52 59 68 55 32 20 43 48 75 30 42 80 60 71
	nb_card = int(s.split(": ")[0].split()[1])
	card = s.split(": ")[1].split(" | ")
	win = card[0].split()
	nb = card[1].split()

	cnt = 0
	for n in nb:
		if n in win:
			cnt += 1
	return nb_card, cnt

counter = 0

list_wins = []
for line in lines:
	n, cnt = parse2(line)
	list_wins.append([1 , n, cnt])
 
print(len(list_wins))
print(list_wins[1][0])

print(list_wins[2][0])

counter = 0
for i in range(len(list_wins)):
	counter += list_wins[i][0]
	for j in range(i + 1, i + list_wins[i][2] + 1):
		list_wins[j][0] += list_wins[i][0]

print(counter)

# dict_cards = {}

# # initialize cards counting dictionary
# for i in range(1, len(lines)):
# 	dict_cards[i] = 0

# def recurscard(ind):
# 	n, cnt = parse2(lines[ind])

# 	i = 0
# 	if cnt == 0:
# 		return 0
# 	for i in range(1, cnt):
# 		if n + i > len(lines) - 1:
# 			return 1
# 		else:
# 			return recurscard(n + i)

# counter = 0
# for i in range(len(lines) - 2):
# 	counter += recurscard(i)

# print(counter)

# tickets = [[1]+[nums.split() for nums in line[9:].split(" | ")] for line in lines]
# print(tickets)
# sumTickets = 0
# for i in range( len(tickets) ):
# 	wins = 0
# 	sumTickets += tickets[i][0]
# 	for win_num in tickets[i][1]:
# 		if win_num in tickets[i][2]:
# 			wins += 1
# 	for j in range(i+1, i+wins+1):
# 		tickets[j][0] += tickets[i][0]    

# print(sumTickets)