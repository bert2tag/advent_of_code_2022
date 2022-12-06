#!/usr/bin/env python3
import sys

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
    charset = []
    n = 0
    for c in data:
        n += 1
        charset.append(c)
        if len(charset) == 14:
            if dupes(charset):
                fourset.pop(0)
            else:
                return n
    return "huh"


for line in sys.stdin.readlines():
    line = line.strip()
    data = [x for x in line]
    marker = scan(data)
    print(marker)
    


