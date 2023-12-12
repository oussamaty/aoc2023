f = open("input.txt")
l = f.readlines()

result = 0

for line in l:
    ll = line.replace('\n', '').split(": ")
    n = ll[0][5:]
    games = ll[1].split("; ")
    nums = [0, 0, 0]
    for game in games:
        vals = game.split(", ")
        for val in vals:
            if val[-3:] == "red":
                nums[0] = max(nums[0], int(val[:-3]))
            elif val[-5:] == "green":
                nums[1] = max(nums[1], int(val[:-5]))
            elif val[-4:] == "blue":
                nums[2] = max(nums[2], int(val[:-4]))
    
    m = nums[0]*nums[1]*nums[2]
    result += m

print(result)