#!/usr/bin/env python3
import numpy as np
import pandas as pd


with open('input.txt') as f:
	lines = f.readlines()

def parse(s):
	time = s[0].split(":")[1].split()
	distance = s[1].split(":")[1].split()
	return time, distance

def count_dist(t):
	tot_d = [(t - i) * i for i in range(t)]
	return tot_d

def get_nb_win(tot_d, d):
	nb_win = sum([1 for n in tot_d if n > d])
	return (nb_win)

time, distance = parse(lines)
cnt = 1
for t, d in zip(time, distance):
	print(t, d)
	cnt *= get_nb_win(count_dist(int(t)), int(d))

print(cnt)

def parse2(s):
	time = ''.join(t for t in s[0].split(":")[1].split())
	distance = ''.join(d for d in s[1].split(":")[1].split())
	return time, distance

t, d = parse2(lines)

print(get_nb_win(count_dist(int(t)), int(d)))