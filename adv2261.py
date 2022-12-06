#!/usr/bin/env python3
import sys
import re


def dupes(chars):
    index = {}
    for c in chars:
        index[c] = 0
    for c in chars:
        index[c] += 1
    for i in index:
        if index[i] > 1:
            return True
    return False
        
        

def scan(data):
    fourset = []
    n = 0
    for c in data:
        n += 1
        fourset.append(c)
        if len(fourset) == 14:
            if dupes(fourset):
                fourset.pop(0)
            else:
                return n
    return "huh"


for line in sys.stdin.readlines():
    line = line.strip()
    data = [x for x in line]
    marker = scan(data)
    print(marker)
    


