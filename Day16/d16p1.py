f = open('Day16/input.txt')
l = f.read().split('\n')

def beam(coords, dir, beams, tiles, visited):
    x, y = coords
    i, j = dir
    while x > -1 and x < len(l) and y > -1 and y < len(l[0]):
        if ((x, y), (i, j)) in visited: return
        tiles.add((x, y))
        visited.add(((x, y), (i, j)))
        if l[x][y] == '/':
            i, j = -j, -i
        elif l[x][y] == '\\':
            i, j = j, i
        elif l[x][y] == '|':
            if i == 0:
                beams.append(((x, y), (-1, 0)))
                beams.append(((x, y), (1, 0)))
                return
        elif l[x][y] == '-':
            if j == 0:
                beams.append(((x, y), (0, -1)))
                beams.append(((x, y), (0, 1)))
                return
        x += i
        y += j

def explore():
    beams = [((0, 0), (0, 1))]
    tiles = set()
    visited = set()

    while beams:
        coords, dir = beams.pop()
        beam(coords, dir, beams, tiles, visited)
    
    return tiles

def display(tiles):
    board = [['.' for j in range(len(l[0]))] for i in range(len(l))]
    for i, j in tiles:
        board[i][j] = '#'
    s = '\n'.join(''.join(board[i]) for i in range(len(board)))
    print(s)

tiles = explore()

result = len(tiles)

print(result)