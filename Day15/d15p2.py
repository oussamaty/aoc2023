f = open('Day15/input.txt')
l = f.read().replace('\n', '').split(',')

def hash_fun(s):
    value = 0
    for c in s:
        value = ((value + ord(c)) * 17) % 256
    return value

def put(s, n, HASHMAP):
    v = hash_fun(s)
    for i in range(len(HASHMAP[v])):
        if s == HASHMAP[v][i][0]:
            HASHMAP[v][i] = (s, n)
            return
    HASHMAP[v].append((s, n))

def remove(s, HASHMAP):
    v = hash_fun(s)
    for i in range(len(HASHMAP[v])):
        if s == HASHMAP[v][i][0]:
            HASHMAP[v].pop(i)
            return
    
def solution():
    HASHMAP = {i: [] for i in range(256)}
    for p in l:
        for i in range(len(p)):
            if p[i] == '-':
                remove(p[:i], HASHMAP)
            if p[i] == '=':
                put(p[:i], int(p[i+1:]), HASHMAP)
    result = 0
    for i in range(256):
        for j in range(len(HASHMAP[i])):
            result += (i + 1) * (j + 1) * HASHMAP[i][j][1]
    return result

print(solution())