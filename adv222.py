#!/usr/bin/env python3
import sys

def value(a):
    if a == 'Rock': return 1
    if a == 'Paper': return 2
    if a == 'Scissors': return 3

def nicename(a):
    if (a == 'A') or (a == 'X'): return 'Rock'
    if (a == 'B') or (a == 'Y'): return 'Paper'
    if (a == 'C') or (a == 'Z'): return 'Scissors'

def win(a,b): 

    if a == 'Rock':
        return b == 'Scissors'
    if a == 'Paper':
        return b == 'Rock'
    if a == 'Scissors':
        return b == 'Paper'

def totals(a,b):
    a = nicename(a)
    b = nicename(b)

    if a == b:
        return 3 + value(a)

    if win(a,b):
        return 6 + value(a)
    else:
        return 0 + value(a)

score = 0
for line in sys.stdin:
    b,a = line.split()
    print("{} {}: {}".format(nicename(a),nicename(b),totals(a,b)))
    score += totals(a,b)
print("score: {}".format(score))
