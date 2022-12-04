#!/usr/bin/env python3
import sys
import pprint

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = {}
n = 1
for c in letters:
    priority[c] = n
    n += 1


def duplicate(ruck1,ruck2):
    index = {}
    dupe = ""
    for c in ruck1:
        index[c] = 1
    for c in ruck2:
        if c in index:
            dupe = c
    return dupe

total = 0
for line in sys.stdin.readlines():
    ruck1 = line[:len(line)//2]
    ruck2 = line[len(line)//2:]
    dupe = duplicate(ruck1,ruck2)
    print(priority[dupe])

    total += priority[dupe]


print("total: {}".format(total))
