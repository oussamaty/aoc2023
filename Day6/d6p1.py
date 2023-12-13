from math import sqrt

f = open('Day6/input.txt')
l = f.readlines()

def t(i):
    return [int(x) for x in l[i].split(': ')[1].strip().split()]
    
times = t(0)
dists = t(1)

result = 1
for i in range(len(times)):
    d = sqrt(times[i]*times[i] - 4*dists[i])
    x, y = (times[i] + d)*0.5 - 0.01, (times[i] - d)*0.5 + 0.01
    result *= int(x) - int(y)

print(result)