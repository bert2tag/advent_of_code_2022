#!/usr/bin/env python3
import sys

def value(a):
    if (a == 'Rock'): return 1
    if (a == 'Paper'): return 2
    if (a == 'Scissors'): return 3

def nicename(a):
    if (a == 'A') or (a == 'X'): return 'Rock'
    if (a == 'B') or (a == 'Y'): return 'Paper'
    if (a == 'C') or (a == 'Z'): return 'Scissors'
    return a

def win(a): 
    if a == 'Rock':
        return 'Scissors'
    if a == 'Paper':
        return 'Rock'
    if a == 'Scissors':
        return 'Paper'

def lose(a):
    if a == 'Rock':
        return 'Paper'
    if a == 'Paper':
        return 'Scissors'
    if a == 'Scissors':
        return 'Rock'

def totals(a,b):
    a = nicename(a)
    if b == 'Y': # draw
        return 3 + value(a)
    if b == 'X': 
        a = win(a)
        return 0 + value(a)
    if b == 'Z': 
        a = lose(a)
        return 6 + value(a)

score = 0
for line in sys.stdin:
    a,b = line.split()
    #print("{} {}".format(nicename(a),b))
    score += totals(a,b)
print("score: {}".format(score))
