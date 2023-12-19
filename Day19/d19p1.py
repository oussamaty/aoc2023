f = open('Day19/input.txt')
l = f.read().split('\n\n')
w, p = l[0].split('\n'), l[1].split('\n')

def get_workflows():
    workflows = {}
    for line in w:
        name, e = line[:-1].split('{')
        workflows[name] = []
        e = e.split(',')
        for ex in e:
            sides = ex.split(':')
            if len(sides) == 1:
                workflows[name].append((ex,))
            else:
                ret = sides[1]
                low = sides[0].split('<')
                high = sides[0].split('>')
                if len(low) == 2:
                    workflows[name].append((low[0], int(low[1]), -1, ret))
                else:
                    workflows[name].append((high[0], int(high[1]), 1, ret))
    return workflows

def get_parts():
    parts = []
    for part in p:
        tmp = {}
        for seg in part[1:-1].split(','):
            key, val = seg.split('=')
            tmp[key] = int(val)
        parts.append(tmp)
    return parts

def check(workflows, part):
    i = 0
    current = 'in'
    while current not in ('A', 'R'):
        instruction = workflows[current][i]
        if len(instruction) == 1:
            current = instruction[0]
            i = 0
            continue
        key, thres, left, ret = instruction
        if left == -1:
            if part[key] >= thres:
                i += 1
                continue
        else:
            if part[key] <= thres:
                i += 1
                continue
        current = ret
        i = 0
    return current

def solution():
    workflows = get_workflows()
    parts = get_parts()
    result = 0

    for part in parts:
        if check(workflows, part) == 'A':
            result += sum(part[x] for x in part)

    return result

result = solution()

print(result)