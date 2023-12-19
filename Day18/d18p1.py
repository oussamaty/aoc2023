f = open("Day18/input.txt")
l = f.read().split('\n')

moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def dig():
    x, y = 0, 0
    path = [(x, y)]
    for line in l:
        dir, m, color = line.split()
        u, v = x + int(m) * moves[dir][0], y + int(m) * moves[dir][1]
        path.append((u, v))
        x, y = u, v
    return path

def area(path):
    a = 0
    for i in range(len(path) - 1):
        a += path[i][0] * path[i + 1][1] - path[i + 1][0] * path[i][1]
    return -a/2

def solution():
    path = dig()
    n = sum(max(abs(path[i + 1][0] - path[i][0]), abs(path[i + 1][1] - path[i][1])) for i in range(len(path) - 1))
    result = int(area(path) + n/2 + 1)
    return result 

result = solution()

print(result)