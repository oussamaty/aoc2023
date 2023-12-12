f = open("input.txt")
l = f.readlines()
nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

result = 0

for line in l:
    tmp = ""

    for i in range(len(line)):
        if line[i].isdigit():
            tmp = line[i]
        elif line[i: i + 3] in nums:
            tmp = nums[line[i: i + 3]]
        elif line[i: i + 4] in nums:
            tmp = nums[line[i: i + 4]]
        elif line[i: i + 5] in nums:
            tmp = nums[line[i: i + 5]]
        else:
            continue
        break
    
    for i in range(1, len(line) + 1):
        if line[-i].isdigit():
            tmp += line[-i]
        elif line[-i - 2: -i + 1] in nums:
            tmp += nums[line[-i - 2: -i + 1]]
        elif line[-i - 3: -i + 1] in nums:
            tmp += nums[line[-i - 3: -i + 1]]
        elif line[-i - 4: -i + 1] in nums:
            tmp += nums[line[-i - 4: -i + 1]]
        else:
            continue
        break

    result += int(tmp)

print(result)