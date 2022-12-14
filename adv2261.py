#!/usr/bin/env python3
import sys

def dupes(chars):
    index = {}
    for c in chars:
        if c in index:
            return True
        index[c] = 0
    return False

def scan(data):
    charset = []
    n = 0
    for c in data:
        n += 1
        charset.append(c)
        if len(charset) == 4:
            if dupes(charset):
                charset.pop(0)
            else:
                return n
    return "huh"


for line in sys.stdin.readlines():
    line = line.strip()
    data = [x for x in line]
    marker = scan(data)
    print(marker)
    


