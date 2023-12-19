f = open("Day18/input.txt")
l = f.read().split('\n')

moves = {
    '3': (-1, 0), # UP
    '1': (1, 0), # DOWN
    '2': (0, -1), # LEFT
    '0': (0, 1) # RIGHT
}

def dig():
    x, y = 0, 0
    path = [(x, y)]
    for line in l:
        dir, m, color = line.split()
        dir = color[-2: -1]
        m = int(color[2:-2], 16)
        u, v = x + m * moves[dir][0], y + m * moves[dir][1]
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