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
                a, b = i, j
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
            return (len(loop) - 1) // 2 + 1
        continue

result = search()

print(result)