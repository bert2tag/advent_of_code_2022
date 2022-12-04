#!/usr/bin/env python3
import sys

def getseq(elf):
    start,finish = elf.split('-')
    sequence =  list(range(int(start),int(finish) + 1))
    return sequence

def list_in_list(s,l):
    len_s = len(s)
    return any(s == l[i:len_s+i] for i in list(range(len(l) - len_s+1)))

def contains(list1,list2):
    return list_in_list(list1,list2) or list_in_list(list2,list1) 

def overlaps(list1,list2):
    for n in list1:
        if n in list2:
            return True
    for n in list2:
        if n in list1:
            return True

conttotal = 0
overtotal = 0
for line in sys.stdin.readlines():
    elf1,elf2 = line.split(',')
    elf1list = getseq(elf1)
    elf2list = getseq(elf2)
    if contains(elf1list,elf2list):
        conttotal += 1
    if overlaps(elf1list,elf2list):
        overtotal += 1


print("c total: {}".format(conttotal))
print("o total: {}".format(overtotal))
