import re
from math import lcm

f = open('Day8/input.txt')
l = f.readlines()

instructions = l[0].strip()
n = len(instructions)
dic = {}

pattern = re.compile(r"([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)")

starts = set()

for line in l:
    match = pattern.match(line)
    if match:
        ind = match.group(1)
        left = match.group(2)
        right = match.group(3)
        dic[ind] = (left, right)
        if ind[-1] == "A":
            starts.add(ind)

def steps(start):
    i = 0
    current = start
    while current[-1] != 'Z':
        if instructions[i % n] == 'L':
            current = dic[current][0]
        else:
            current = dic[current][1]
        i += 1
    return i

s = [steps(start) for start in starts]
result = lcm(*s)

print(result)