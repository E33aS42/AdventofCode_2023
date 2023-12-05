#!/usr/bin/env python3
import numpy as np
import pandas as pd
import re


def parse(s):
	# Game 1: 1 blue, 1 red; 10 red; 8 red, 1 blue, 1 green; 1 green, 5 blue
	game = int(s.split(": ")[0].split(" ")[1])

	str = s.split(": ")[1].split("\n")[0].split("; ")

	dicolor = {"red": 0, "green": 0, "blue": 0}

	for e in str:
		e1 = e.split(", ")
		for e2 in e1:
			e3 = e2.split(" ")
			if dicolor[e3[1]] < int(e3[0]):
				dicolor[e3[1]] = int(e3[0])

	return game, dicolor

def parse2(s):
	# Game 1: 1 blue, 1 red; 10 red; 8 red, 1 blue, 1 green; 1 green, 5 blue
	game = int(s.split(": ")[0].split(" ")[1])

	str = s.split(": ")[1].split("\n")[0].split("; ")

	dicolor = {"red": -1, "green": -1, "blue": -1}

	for e in str:
		e1 = e.split(", ")
		for e2 in e1:
			e3 = e2.split(" ")
			if dicolor[e3[1]] < int(e3[0]):
				dicolor[e3[1]] = int(e3[0])

	return game, dicolor

with open('input.txt') as f:
	lines = f.readlines()

final = 0
for line in lines:
	bad = 0
	game, dicolor = parse(line)
	colors = list(dicolor.keys())
	dicolors = {"red": 12, "green": 13, "blue": 14}
	for c in colors:
		if dicolor[c] > dicolors[c]:
			bad = 1
			break
	if bad == 0:
		final += game


print(final)

final2 = 0
for line in lines:
	bad = 0
	game, dicolor = parse2(line)
	colors = list(dicolor.keys())
	final2 += dicolor[colors[0]] * dicolor[colors[1]] * dicolor[colors[2]]

print(final2)