f = open('Day14/input.txt')
l = f.read().split('\n')
n = len(l)

def get_indices():
    support = [[] for i in range(len(l[0]))]
    rocks = [[] for i in range(len(l[0]))]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == '#':
                support[j].append(i)
            if l[i][j] == 'O':
                rocks[j].append(i)
    return support, rocks

def side(s):
    p = [[] for i in range(n)]
    for i in range(len(s)):
        for x in s[i]:
            p[x].append(i)
    return p

def flip(s):
    p = [[] for i in range(len(s))]
    for i in range(len(s)):
        for x in s[i][::-1]:
            p[i].append(len(s) - x - 1)
    return p

def tilt(support, rocks):
    result = [[] for i in range(len(rocks))]
    for j in range(len(rocks)):
        sind = 0
        level = -1
        for i in rocks[j]:
            for k in range(sind, len(support[j])):
                if i < support[j][k]: break
                level = max(support[j][k], level)
            if sind != len(support[j]):
                sind = k
            level += 1
            result[j].append(level)
    return support, result

def show(support, rocks):
    display = ['.' * n  for i in range(n)]
    for i in range(len(support)):
        for x in support[i]:
            display[x] = display[x][:i] + '#' + display[x][i + 1:]
        for x in rocks[i]:
            display[x] = display[x][:i] + 'O' + display[x][i + 1:]
    display = '\n'.join(display)
    print(display)
    print('------------------------------')


def cycle(support, rocks):
    nsupport, nrocks = tilt(support, rocks)
    nsupport, nrocks = side(nsupport), side(nrocks)
    nsupport, nrocks = tilt(nsupport, nrocks)
    nsupport, nrocks = side(nsupport), side(nrocks)
    nsupport, nrocks = flip(nsupport),  flip(nrocks)
    nsupport, nrocks = tilt(nsupport, nrocks)
    nsupport, nrocks = flip(nsupport),  flip(nrocks)
    nsupport, nrocks = side(nsupport), side(nrocks)
    nsupport, nrocks = flip(nsupport),  flip(nrocks)
    nsupport, nrocks = tilt(nsupport, nrocks)
    nsupport, nrocks = flip(nsupport),  flip(nrocks)
    nsupport, nrocks = side(nsupport), side(nrocks)
    return nsupport, nrocks

def hashable(current):
    return tuple(tuple(x for x in current[i]) for i in range(len(current)))

def calculate_load(rocks):
    result = 0
    for j in range(len(rocks)):
        for x in rocks[j]:
            result += len(rocks) - x
    return result

def find_cycle(N):
    memo = {}
    nsupport, nrocks = get_indices()
    for i in range(N):
        hrocks = hashable(nrocks)
        if hrocks in memo:
            return i + 1, memo[hrocks], nsupport, nrocks
        nsupport, nrocks = cycle(nsupport, nrocks)
        memo[hrocks] = i + 1


def solution():
    N = 1000000000
    p, b, nsupport, nrocks = find_cycle(N)
    ind = (N - b) % (p - b)
    for i in range(ind + 1):
        nsupport, nrocks = cycle(nsupport, nrocks)
    return calculate_load(nrocks)

print(solution())