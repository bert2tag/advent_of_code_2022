#!/usr/bin/env python3
import sys
import re

def consume(line,data):
    line = line.rstrip()
    column = 4
    columns = [line[i:i+column] for i in range(0, len(line), column)]
    n = 1
    for column in columns:
        if not n in data:
            data[n] = []
        column = column.replace('[','')
        column = column.replace(']','')
        column = column.strip()
        if column != '':
            data[n].append(column)
        n += 1
    return data

def tops(data):
    result = ""
    for i in data:
        result += data[i].pop()
    return result

def invert(data):
    for i in data:
        data[i].reverse()
    return data

def move9000(line,data):
    movement = re.findall(r'\d+',line)
    ints = [eval(i) for i in movement]
    howmany,fromcol,tocol = tuple(ints)
    for i in range(howmany):
        item = data[fromcol].pop()
        data[tocol].append(item)
    return data

def move9001(line,data):
    movement = re.findall(r'\d+',line)
    ints = [eval(i) for i in movement]
    howmany,fromcol,tocol = tuple(ints)
    items = []
    for i in range(howmany):
        items.insert(0,data[fromcol].pop())
    data[tocol] += items
    return data

data = {}
for line in sys.stdin.readlines():

    if 'move' in line:
        data = move9001(line,data)

    if ' 1 ' in line and not 'move' in line:
        data = invert(data)

    if '[' in line:
        data = consume(line,data)

result = tops(data)
print(result)

