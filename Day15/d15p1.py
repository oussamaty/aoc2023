f = open('Day15/input.txt')
l = f.read().replace('\n', '').split(',')

def hash_fun(s):
    value = 0
    for c in s:
        value = ((value + ord(c)) * 17) % 256
    return value

result = 0
for s in l:
    result += hash_fun(s)

print(result)