f = open('Day3/input.txt')
ll = f.readlines()
result = 0

for i in range(len(ll)):
    for j in range(len(ll[i])):
        if ll[i][j] == '*':
            tmp = set()
            for k in [-1, 0, 1]:
                for kk in [-1, 0, 1]:
                    if not (k == 0 and kk == 0) and i + k < len(ll) and i + k > -1 and j + kk < len(ll[i + k]) and j + kk > -1:
                        x, y = i + k, j + kk
                        if ll[x][y].isdigit():
                            start, end = y, y
                            changed = True
                            while changed:
                                changed = False
                                if start > 0 and ll[x][start - 1].isdigit():
                                    start -= 1
                                    changed = True
                                if end < len(ll[x]) - 1 and ll[x][end + 1].isdigit():
                                    end += 1
                                    changed = True
                            tmp.add((x, start, end))
            if len(tmp) == 2:
                p = 1
                for x, start, end in tmp:
                    n = int(ll[x][start:end + 1])
                    p *= n
                result += p

print(result)