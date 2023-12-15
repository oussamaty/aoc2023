f = open('Day13/input.txt')
l = f.read().split('\n\n')

segs = [part.split('\n') for part in l]

def line_reflexion():
    cols, rows = [[] for k in range(len(segs))], [[] for k in range(len(segs))]
    for k in range(len(segs)):
        for i in range(len(segs[k]) - 1):
            reflexion = True
            for j in range(len(segs[k][i])):
                if segs[k][i][j] != segs[k][i + 1][j]:
                    reflexion = False
                    break
            if reflexion:
                rows[k].append(i)
        
        for j in range(len(segs[k][0]) - 1):
            reflexion = True
            for i in range(len(segs[k])):
                if segs[k][i][j] != segs[k][i][j + 1]:
                    reflexion = False
                    break
            if reflexion:
                cols[k].append(j)
    return cols, rows
    
def full_reflexion():
    result = [0]*len(segs)
    cols, rows = line_reflexion()
    for k in range(len(cols)):
        if len(cols[k]) == 0: continue
        for col in cols[k]:
            reflexion = True
            for y in range(1, min(col + 1, len(segs[k][0]) - col - 1)):
                for i in range(len(segs[k])):
                    if segs[k][i][col - y] != segs[k][i][col + 1 + y]:
                        reflexion = False
                        break
            if reflexion:
                result[k] = (col, -1)
                break

    for k in range(len(rows)):
        if len(rows[k]) == 0: continue
        for row in rows[k]:
            reflexion = True
            for x in range(1, min(row + 1, len(segs[k]) - row - 1)):
                for j in range(len(segs[k][0])):
                    if segs[k][row - x][j] != segs[k][row + 1 + x][j]:
                        reflexion = False
                        break
            if reflexion:
                result[k] = (-1, row)
                break   
    
    return result   

def score():
    s = 0
    result = full_reflexion()
    for col, row in result:
        s += col + 1 + (row + 1)*100
    return s

print(score())