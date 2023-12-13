f = open('Day4/input.txt')
l = f.readlines()
result = 0

for line in l:
    ll = line.replace('\n', '').split(': ')
    n = ll[0][5:]
    cards = ll[1].split(' | ')
    wnums = set(cards[0].split())
    pnums = set(cards[1].split())
    if len(wnums.intersection(pnums)) > 0:
        result += 2**(len(wnums.intersection(pnums)) - 1)

print(result)