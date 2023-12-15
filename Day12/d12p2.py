f = open('Day12/input.txt')
l = f.read().split('\n')

puzzles = []

for line in l:
    parts = line.split()
    puzzle = list(parts[0])
    check = [int(x) for x in parts[1].split(',')]
    ind = set()
    for i in range(len(puzzle)):
        if puzzle[i] == '?':
            ind.add(i)
    puzzles.append((puzzle, parts[0], ind, check))

def correct(current):
    r = []
    t = 0
    for c in '.' + current + '.':
        if c == '.' and t == -1:
            r.append(t)
            t = 0
        if c == '#' and t > -1:
            t += 1
        if c == '?':
            t = -1
        if c == '.' and t > 0:
            r.append(t)
            t = 0
    return r

def explore(ind, current, currentS, check, memo):
    if len(ind) == 0:
        c = 1
        r = correct(currentS)
        if len(r) != len(check):
            c = 0
        else:
            for i in range(len(r)):
                if r[i] != check[i]:
                    c = 0
        memo[currentS] = c
        return c

    currentC = correct(currentS)

    exploreC = True
    if len(list(filter(lambda x: x > -1, currentC))) > len(check):
        exploreC = False
    else:
        for i in range(len(currentC)):
            if currentC[i] < 0: break
            if currentC[i] != check[i]:
                exploreC = False
            
        for i in range(-1, -len(currentC) - 1, -1):
            if currentC[i] < 0: break
            if currentC[i] != check[i]:
                exploreC = False
    
    if not exploreC:
        memo[currentS] = 0
        return 0

    for i in ind:
        nind = ind.copy()
        nind.remove(i)
        left = [*current]
        right = [*current]
        left[i] = '.'
        right[i] = '#'
        leftS = ''.join(left)
        rightS = ''.join(right)
        
        le, re = 0, 0

        if leftS in memo:
            le = memo[leftS]
        else:
            le = explore(nind, left, leftS, check, memo)
        
        if rightS in memo:
            re = memo[rightS]
        else:
            re = explore(nind, right, rightS, check, memo)

        memo[currentS] = le + re
        return memo[currentS]

result = 0

for i in range(len(puzzles)):
    memo = {}
    puzzle, puzzleS, ind, check = puzzles[i]
    g = explore(ind, puzzle, puzzleS, check, memo)
    result += g

print(result)