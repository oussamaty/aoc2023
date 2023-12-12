f = open('input.txt')
l = f.readlines()
result = 0

games = []

for line in l:
    ll = line.replace('\n', '').split(': ')
    n = ll[0][5:]
    cards = ll[1].split(' | ')
    wnums = set(cards[0].split())
    pnums = set(cards[1].split())
    games.append(len(wnums.intersection(pnums)))

a = [1]*len(games)
for i in range(2, len(games) + 1):
    for j in range(1, games[-i] + 1):
        a[-i] += a[-i + j]

result = sum(a)
print(result)