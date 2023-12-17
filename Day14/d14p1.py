f = open('Day14/input.txt')
l = f.read().split('\n')

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

def tilt(support, rocks):
    result = 0
    for j in range(len(rocks)):
        sind = 0
        level = -1
        for i in rocks[j]:
            for k in range(sind, len(support[j])):
                if i < support[j][k]: break
                level = max(support[j][k], level)
            sind = k
            level += 1
            result += len(rocks) - level
    return result

support, rocks = get_indices()
result = tilt(support, rocks)

print(result)