f = open('Day7/input.txt')
l = f.readlines()

t = 1
order = {}
for c in "23456789TJQKA":
    order[c] = t
    t += 1

hands = []

for line in l:
    s = line.split()
    hands.append((s[0], int(s[1])))

def rank(x):
    d = {}
    for c in x:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    for c in d:
        if d[c] == 5:
            return 10
        if d[c] == 4:
            return 9
        if d[c] == 3 and len(d) == 2:
            return 8
        if d[c] == 3 and len(d) == 3:
            return 7
        if d[c] == 2 and len(d) == 2:
            return 8
        if d[c] == 2 and len(d) == 3:
            return 6
        if d[c] == 2 and len(d) == 4:
            return 5
        if d[c] == 1 and len(d) == 2:
            return 9
        if d[c] == 1 and len(d) == 3:
            continue
        if d[c] == 1 and len(d) == 4:
            return 5
        return 4
        
def comp(x):
    return (rank(x), ) + tuple([order[c] for c in x])

ranks = sorted(hands, key=lambda x: comp(x[0]))

result = 0
for i in range(len(ranks)):
    result += (i + 1)*ranks[i][1]

print(result)