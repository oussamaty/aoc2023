from collections import deque

f = open('Day20/input.txt')
l = f.read().split('\n')

def get_modules():
    modules = {}
    conjenctions = {}
    for line in l:
        module, rest = line.split(' -> ')
        outputs = rest.split(', ')
        if module[0] == '%':
            modules[module[1:]] = [1, 0, outputs]
        elif module[0] == '&':
            modules[module[1:]] = [2, 0, outputs]
        else:
            modules[module] = [0, 0, outputs]
    for module in modules:
        if modules[module][0] == 2:
            conjenctions[module] = {other: 0 for other in modules if module in modules[other][2]}
    return modules, conjenctions

def push_button(modules, conjenctions):
    result = {0: 0, 1: 0}
    entry = 'broadcaster'
    queue = deque([(entry, entry, 0)])
    while queue:
        sender, node, pulse = queue.popleft()
        result[pulse] += 1
        if node not in modules:
            modules[node] = (-1, 0, [])
        typ, state, outputs = modules[node]
        if typ == 1:
            if pulse == 0:
                state = ((state + 1) % 2)
                modules[node][1] = state
                for output in outputs:
                    queue.append((node, output, state))
        elif typ == 2:
            out = 0
            conjenctions[node][sender] = pulse
            for m in conjenctions[node]:
                if conjenctions[node][m] == 0:
                    out = 1
                    break
            for output in outputs:
                queue.append((node, output, out))
        else:
            for output in outputs:
                queue.append((node, output, pulse))
    return result

def solution(n):
    modules, conjenctions = get_modules()
    low, high = 0, 0
    for i in range(n):
        count = push_button(modules, conjenctions)
        low += count[0]
        high += count[1]
    return low * high

result = solution(1000)

print(result)