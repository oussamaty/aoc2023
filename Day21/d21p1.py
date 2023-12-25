from collections import deque

f = open('Day21/input.txt')
l = f.read().split('\n')

def get_start():
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == 'S':
                return (i, j)

def steps(n):
    start = get_start()
    queue = deque([(start, 0)])
    visited = {0: set(), 1: set()}
    while queue:
        current, level = queue.popleft()
        if level > n:
            return len(visited[n % 2])
        if current in visited[0] or current in visited[1]: continue
        visited[(current[0] + current[1]) % 2].add((current))
        for k in (-1, 1):
            if current[0] + k < len(l) and current[0] + k > -1 and l[current[0] + k][current[1]] != '#':
                queue.append(((current[0] + k, current[1]), level + 1))
            if current[1] + k < len(l[0]) and current[1] + k > -1 and l[current[0]][current[1] + k] != '#':
                queue.append(((current[0], current[1] + k), level + 1))
    return -1

result = steps(64)

print(result)