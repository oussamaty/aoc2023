f = open("Day1/input.txt")
l = f.readlines()

result = 0

for line in l:
    tmp = ""
    for i in range(len(line)):
        if line[i].isdigit():
            tmp = line[i]
            break
    for i in range(1, len(line) + 1):
        if line[-i].isdigit():
            tmp += line[-i]
            break
    result += int(tmp)

print(result)