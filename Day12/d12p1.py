from functools import cache

f = open('Day12/input.txt')
l = f.read().split('\n')

def sequences():
    puzzles = []
    for line in l:
        parts = line.split()
        puzzle = parts[0]
        check = tuple(int(x) for x in parts[1].split(','))
        puzzles.append((puzzle, check))
    return puzzles

@cache
def search(puzzle, check):
    springs = (f"{s*'.'}{'#'*check[0]}." for s in range(len(puzzle) - sum(check) - len(check) + 1))
    valid = (len(s) for s in springs if all(r in (c, '?') for r, c in zip(puzzle, s)))
    if len(check) > 1:
        return sum(search(puzzle[i:], check[1:]) for i in valid)
    return sum('#' not in puzzle[i:] for i in valid)

result = sum(search(puzzle + '.', check) for puzzle, check in sequences())
print(result)