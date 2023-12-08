#!/usr/bin/env python3
import copy

with open('input.txt') as f:
	lines = f.readlines()

with open('ex') as f:
	lines = f.readlines()
	
def parse(line):
	s = line.split()
	return s[0], s[1]

def get_type(hand, cnt_cards):

	for k in list(cnt_cards.keys()):
		cnt_cards[k] = hand.count(k)

	cards = {key: value for key, value in cnt_cards.items() if int(value) > 0}
	val_cards = sorted(cards.values())

	# check types
	if val_cards == [5]:
		return 7, hand
	elif val_cards == [1, 4]:
		return 6, hand
	elif val_cards == [2, 3]:
		return 5, hand
	elif val_cards == [1, 1, 3]:
		return 4, hand
	elif val_cards == [1, 2, 2]:
		return 3, hand
	elif val_cards == [1, 1, 1, 2]:
		return 2, hand
	else:
		return 1, hand

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
zero = [0 for _ in range(len(cards))]
rate_cards = dict(zip(cards, zero))

i = 0
for k in rate_cards.keys():
	rate_cards[k] = chr(ord('2') + i)
	i += 1

val = rate_cards.values()
cnt_cards = dict(zip(val, zero))

# print(rate_cards)
# {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'T': ':', 'J': ';', 'Q': '<', 'K': '=', 'A': '>'}
game = []
for line in lines:
	hand, bid = parse(line)
	
	for k in rate_cards.keys():
		hand_sorted = hand.replace(k, rate_cards[k])
	hand_sorted = "".join([i for i in sorted(hand_sorted, reverse = True)])
	game.append((hand, bid))

game = sorted(game, key=lambda x:get_type(x[0], cnt_cards))

print(game)

score = 0
for i, (hand, bid) in enumerate(game):
	score += int(bid) * (i + 1)

print(score)