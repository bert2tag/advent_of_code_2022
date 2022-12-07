#!/usr/bin/env python3
import sys
import re


cmd_m = re.compile(r'^\$ cd (.+)$')
file_m = re.compile(r'^(\d+) (.+)$')

#preprocess
lines = []
for line in sys.stdin.readlines():
    line = line.strip()
    lines.append(line)

device = {}
index = 0
for line in lines:
    #print(line)
    cmd = re.match(cmd_m,line)
    isfile = re.match(file_m,line)
    if cmd:
        if 'cd ' in line and '..' not in line:
            index += 1
            cwd = cmd.group(1)
            device[index] = 0
            print('index:{} {}'.format(cwd,index))
        elif 'cd ..' in line:
            index = index - 1
    if isfile:
        size = isfile.group(1)
        name = isfile.group(2)
        device[index] += int(size)
            
print(device)
        


