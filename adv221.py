#!/usr/bin/env python3
import sys
import pprint

def top_3(elfs):
    elf_data = list(elfs.values())
    
    elf_data.sort()
    return elf_data

def max_elf(elfs):
    maxcals = 0
    maxelf = 0
    for elf in elfs:
        if elfs[elf] > maxcals:
            maxcals = elfs[elf]
            maxelf = elf
        
    return maxelf,maxcals

def has_num(s):
    return any(i.isdigit() for i in s)

pp = pprint.PrettyPrinter(indent=4)

elfs = {}
elfname = 1
for line in sys.stdin:
    if has_num(line):
        if elfname in elfs:
            elfs[elfname] += int(line)
        else:
            elfs[elfname] = int(line)
    else:
        elfname += 1
        
#        print("xx:{}".format(line))
#        print("en:{}".format(elfname))
#        print("ee:{}".format(elfname))
#pp.pprint(elfs)
maxelf,maxcals = max_elf(elfs)
print("elf {}, cals: {}".format(maxelf,maxcals))
top3tot = sum(top_3(elfs)[-3:])
print("top3 total: {}".format(top3tot))

