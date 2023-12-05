#!/usr/bin/env python3
import numpy as np
import pandas as pd
from io import StringIO
import re
import itertools as it

title = ["seeds", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

with open('input.txt') as f:
	contents = f.read()
	i = 0
	dict_ = {}
	for entry in contents.split('\n\n'):
		dict_[title[i]] = entry
		i += 1


seed = dict_[title[0]].split(": ")[1].split()
soil = pd.read_csv(StringIO(dict_[title[1]].split(":\n")[1]), header = None)
fertilizer = pd.read_csv(StringIO(dict_[title[2]].split(":\n")[1]), header = None)
water = pd.read_csv(StringIO(dict_[title[3]].split(":\n")[1]), header = None)
light = pd.read_csv(StringIO(dict_[title[4]].split(":\n")[1]), header = None)
temperature = pd.read_csv(StringIO(dict_[title[5]].split(":\n")[1]), header = None)
humidity = pd.read_csv(StringIO(dict_[title[6]].split(":\n")[1]), header = None)
location = pd.read_csv(StringIO(dict_[title[7]].split(":\n")[1]), header = None)

print(location)

# def parse(s):