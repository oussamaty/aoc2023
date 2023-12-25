from collections import deque

f = open('Day21/input.txt')
l = f.read().split('\n')

def get_start():
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == 'S':
                return (i, j)

def steps(start, n):
    queue = deque([(start, 0)])
    visited = {0: set(), 1: set()}
    while queue:
        current, level = queue.popleft()
        if level > n:
            return len(visited[n % 2])
        if current in visited[0] or current in visited[1]: continue
        visited[(current[0] + current[1]) % 2].add((current))
        for k in (-1, 1):
            if l[(current[0] + k) % len(l)][current[1] % len(l)] != '#':
                queue.append(((current[0] + k, current[1]), level + 1))
            if l[current[0] % len(l)][(current[1] + k) % len(l)] != '#':
                queue.append(((current[0], current[1] + k), level + 1))
    return -1

def solution(N):
    n = len(l)
    start = get_start()
    y = [steps(start, n // 2 + i * n) for i in range(3)]
    a = (y[2] - 2 * y[1] + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    x = (N - n // 2) // n
    result = a * (x * x) + b * x + c
    return result

result = solution(26501365)

print(result)