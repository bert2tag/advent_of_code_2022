#!/usr/bin/env python3
import sys

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = {}
n = 1
for c in letters:
    priority[c] = n
    n += 1

def rucks3(l):
    for i in range(0, len(l), 3):
        yield l[i:i + 3]

def compare(trio):
    index = {}
    for ruck in trio:
        ruck = "".join(set(ruck))
        for char in ruck:
            if char in index:
                index[char] += 1
            else:
                index[char] = 1
            if index[char] == 3:
                return char

lines = []
for line in sys.stdin.readlines():
    line = line.strip()
    lines.append(line)


total = 0
for trio in rucks3(lines):
    total += priority[compare(trio)]

print(total)

