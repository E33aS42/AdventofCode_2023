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

with open('input.txt') as f:
	lines = f.readlines()

# Part 1

dicolors = {"red": 12, "green": 13, "blue": 14}
final = 0
for line in lines:
	game, dicolor = parse(line)
	colors = list(dicolor.keys())
	bad = 0
	for c in colors:
		if dicolor[c] > dicolors[c]: bad = 1; break
	# for c in colors: bad = 1 if dicolor[c] > dicolors[c] else 0
	if bad == 0:
		final += game

print(final)


# Part 2

final2 = 0
for line in lines:
	game, dicolor = parse(line)
	colors = list(dicolor.keys())
	final2 += dicolor[colors[0]] * dicolor[colors[1]] * dicolor[colors[2]]

print(final2)