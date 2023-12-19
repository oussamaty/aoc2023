import heapq
f = open('Day17/input.txt')
l = f.read().split('\n')

left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)

def display(path):
    s = [[l[i][j] for j in range(len(l[0]))] for i in range(len(l))]
    for i in range(1, len(path)):
        x = path[i][0] - path[i - 1][0]
        y = path[i][1] - path[i - 1][1]
        if (x, y) == (0, 1):
            s[path[i][0]][path[i][1]] = '>'
        if (x, y) == (0, -1):
            s[path[i][0]][path[i][1]] = '<'
        if (x, y) == (1, 0):
            s[path[i][0]][path[i][1]] = 'v'
        if (x, y) == (-1, 0):
            s[path[i][0]][path[i][1]] = '^'
    
    r = '\n'.join(''.join(s[i][j] for j in range(len(s[0]))) for i in range(len(s)))
    print(r)

def valid(node):
    return node[0] > -1 and node[1] > -1 and node[0] < len(l) and node[1] < len(l[0])

def get_neighbors(orient):
    if orient == left or orient == right:
        yield up
        yield down
    elif orient == up or orient == down:
        yield left
        yield right
    else:
        yield right
        yield down

def solution(src, dest, dmin, dmax):
    queue = [(0, src, (0, 0))]
    visited = set()

    while queue:
        d, u, o = heapq.heappop(queue)

        if u == dest: return d
        
        if (u, o) in visited: continue
        visited.add((u, o))

        for v in get_neighbors(o):
            alt = d
            for i in range(1, dmax + 1):
                w = (u[0] + i*v[0], u[1] + i*v[1])
                if not valid(w): continue
                alt += int(l[w[0]][w[1]])
                if dmin <= i:
                    heapq.heappush(queue, (alt, w, v))
    return d

result = solution((0, 0), (len(l) - 1, len(l[0]) - 1), 4, 10)

print(result)