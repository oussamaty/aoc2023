f = open("Day9/input.txt")
l = f.readlines()
result = 0

for line in l:
    diffs = [[int(x) for x in line.split()]]
    while not (diffs[-1][0] == 0 and diffs[-1][-1] == 0):
        diffs.append([diffs[-1][i + 1] - diffs[-1][i] for i in range(len(diffs[-1]) - 1)])
    result += sum(diffs[i][0] for i in range(0, len(diffs), 2)) - sum(diffs[i][0] for i in range(1, len(diffs), 2))

print(result)