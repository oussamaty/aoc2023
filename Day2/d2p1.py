f = open("Day2/input.txt")
l = f.readlines()

threshold = [12, 13, 14]

result = 0

for line in l:
    ll = line.replace('\n', '').split(": ")
    n = ll[0][5:]
    games = ll[1].split("; ")
    check = True
    for game in games:
        vals = game.split(", ")
        for val in vals:
            if val[-3:] == "red" and int(val[:-3]) > threshold[0]:
                check = False
                break
            elif val[-5:] == "green" and int(val[:-5]) > threshold[1]:
                check = False
                break
            elif val[-4:] == "blue" and int(val[:-4]) > threshold[2]:
                check = False
                break
        if not check:
            break
    if check:
        result += int(n)
            
print(result)