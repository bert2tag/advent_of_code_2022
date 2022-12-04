#!/usr/bin/env python3
import sys
import pprint


def getseq(elf):
    start,finish = elf.split('-')
    #print("SF: {}-{}".format(start,finish))
    sequence =  list(range(int(start),int(finish) + 1))
    #print("SQ: {}".format(sequence))
    return sequence

def list_in_list(s,l):
    len_s = len(s)
    return any(s == l[i:len_s+i] for i in list(range(len(l) - len_s+1)))

def contains(list1,list2):
    return list_in_list(list1,list2) or list_in_list(list2,list1) 

total = 0
for line in sys.stdin.readlines():
    elf1,elf2 = line.split(',')
    elf1list = getseq(elf1)
    elf2list = getseq(elf2)
    if contains(elf1list,elf2list):
        total += 1
        print("EL: {}-{}".format(elf1list,elf2list))


print("total: {}".format(total))
