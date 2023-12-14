f = open('Day10/input.txt')
l = f.read().split('\n')

connections = {
    (0, -1): ['|', '7', 'F'],
    (0, 1): ['|', 'L', 'J'],
    (1, 0): ['-', 'J', '7'],
    (-1, 0): ['-', 'L', 'F']
}

directions = {
    '|': [(0, 1), (0, -1)], 
    '-': [(1, 0), (-1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)]
}

def next(i, j, d):
    for y, x in directions[l[i][j]]:
        if (i + x, j + y) in d: continue
        if i + x > len(l) - 1 or i + x < 0: continue
        if j + y > len(l[i + x]) - 1 or j + y < 0: continue
        if l[i + x][j + y] in connections[(y, x)]:
            return (i + x, j + y)

def start():
    starts = set()
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == 'S':
                for y, x in connections:
                    if i + x > len(l) - 1 or i + x < 0: continue
                    if j + y > len(l[i + x]) or j + y < 0: continue
                    if l[i + x][j + y] in connections[(y, x)]:
                        starts.add((i + x, j + y))
                return (i, j), starts

def search():
    s, starts = start()
    for node in starts:
        inital = starts - set([node])
        current = node
        loop = set([s, current])
        while current not in inital:
            current = next(current[0], current[1], loop)
            if current == None:
                break
            loop.add(current)
        else:
            return loop, s
        continue

def board(loop, a):
    b = [["."]*(len(l[0])*2 + 1)]
    for i in range(len(l)):
        s = ["."]
        for j in range(len(l[i])):
            s.append(l[i][j])
            s.append(".")
        b.append(s)
        b.append(['.']*len(s))
    
    new_loop = set([(2*a[0] + 1, 2*a[1] + 1)])

    for (i, j) in (loop - set([a])):
        new_loop.add((2*i + 1, 2*j + 1))
        for y, x in directions[l[i][j]]:
            b[2*i + x + 1][2*j + y + 1] = connections[(y, x)][0]
            new_loop.add((2*i + x + 1, 2*j + y + 1))

    return b, new_loop

def dfs(s, c, d, v):
    p = set([s])
    while p:
        i, j = p.pop()
        if (i,j) not in c:
            d[(i, j)] = v
        for y, x in connections:
            if i + x > len(b) - 1 or i + x < 0: continue
            if j + y > len(b[i + x]) - 1 or j + y < 0: continue
            if (i + x, j + y) in c: continue
            if (i + x, j + y) in d: continue
            p.add((i + x, j + y))

def groups(loop):
    t = 0
    d = {}
    for i in range(len(b)):
        for j in range(len(b[i])):
            if (i, j) not in d and (i, j) not in loop:
                dfs((i, j), loop, d, t)
                t += 1
    return d

loop, s = search()

b, new_loop = board(loop, s)
g = groups(new_loop)

result = 0

for i in range(len(l)):
    for j in range(len(l[i])):
        if (2*i + 1, 2*j + 1) in g and g[(2*i + 1, 2*j + 1)] == 1:
            result += 1

print(result)