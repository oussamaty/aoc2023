import re

f = open('Day8/input.txt')
l = f.readlines()

instructions = l[0].strip()
n = len(instructions)
dic = {}

pattern = re.compile(r"([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)")

for line in l:
    match = pattern.match(line)
    if match:
        ind = match.group(1)
        left = match.group(2)
        right = match.group(3)
        dic[ind] = (left, right)

start = "AAA"
end = "ZZZ"

i = 0
current = start
while current != end:
    if instructions[i % n] == 'L':
        current = dic[current][0]
    else:
        current = dic[current][1]
    i += 1

print(i)