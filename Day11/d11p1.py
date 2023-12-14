f = open('Day11/input.txt')
l = f.read().split('\n')

pos = []
mark = [set(), set()]

for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == "#":
            pos.append((i, j))
            mark[0].add(i)
            mark[1].add(j)

ind = [[0]*len(l), [0]*len(l[0])]
for i in range(1, len(l)):
    if i in mark[0]:
        ind[0][i] = ind[0][i - 1] + 1
    else:
        ind[0][i] = ind[0][i - 1] + 2
for i in range(1, len(l[0])):
    if i in mark[1]:
        ind[1][i] = ind[1][i - 1] + 1
    else:
        ind[1][i] = ind[1][i - 1] + 2

result = 0
for i in range(len(pos)):
    for j in range(i + 1, len(pos)):
        result += abs(ind[0][pos[j][0]] - ind[0][pos[i][0]]) + abs(ind[1][pos[j][1]] - ind[1][pos[i][1]])

print(result)