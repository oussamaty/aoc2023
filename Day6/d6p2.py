from math import sqrt

f = open('Day6/input.txt')
l = f.readlines()

def t(i):
    return int(''.join(l[i].split(': ')[1].strip().split()))
    
time = t(0)
dist = t(1)

result = 1
d = sqrt(time*time - 4*dist)
x, y = (time + d)*0.5 - 0.01, (time - d)*0.5 + 0.01
result *= int(x) - int(y)

print(result)