f = open('Day5/input.txt')
r = f.read()

parts = r.split('\n\n')

def t(n):
    return sorted([[int(x) for x in l.split()] for l in parts[n].split('\n')[1:]], key=lambda x: x[1])

def o(h):
    start, end = 0, len(h) - 1
    for i in range(len(h)):
        if h[i][2] == 0:
            start = i
            break
    
    for i in range(len(h) - 1, -1, -1):
        if h[i][2] == 0:
            end = i
            break

    k = []
    a, b, c = h[0]

    if start % 2 == 1:
        a, b, c = h[start - 1]
    else:
        a, b, c = h[start]
        start += 1

    for i in range(start, end + 1):
        x, y, z = h[i]
        if c == 1:
            if z == 0:
                a, b, c = x, b + (x - a), 2
            else:
                a, b, c = x, y, -1
        elif c == 0:
            if z == 0:
                k.append((a, x - a + 1))
                a, b = x, y
                c = -1
            else:
                k.append((a, x - a))
                a, b = x, y
                c = 2
        elif c == 2:
            if z == 0:
                k.append((b, x - a + 1))
                c = 1
            else:
                k.append((b, x - a + 1))
                a, b = x, y
                c = -2
        elif c == -1:
            a, b = x, y
            c = z
        elif c == -2:
            if z == 0:
                k.append((a + 1, x - a))
                a, b = x, y
                c = -1
            else:
                a, b = x, y
                c = 2
    
    return list(filter(lambda x: x[1] != 0, k))

def w(s, d):
    h = []
    for x, r in s:
        h.append((x, x, 0))
        h.append((x + r - 1, x + r - 1, 0))
    for a, b, c in d:
        h.append((b, a, 1))
        h.append((b + c - 1, a + c - 1, 1))
    h = sorted(h, key=lambda x: x[0])
    k = o(h)
    return sorted(k, key=lambda x: x[0])

seeds = [int(x) for x in parts[0][7:].split()]
result = [(seeds[i], 1) for i in range(len(seeds))]

for i in range(7):
    result = w(result, t(i + 1))

print(result[0][0])