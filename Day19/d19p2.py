f = open('Day19/input.txt')
l = f.read().split('\n\n')

class Interval:
    def __init__(self, boundaries = {}):
        self.limits = {
            'x': [1, 4000],
            'm': [1, 4000],
            'a': [1, 4000],
            's': [1, 4000]
        }
        self.boundaries = {}
        self.fill(boundaries)
    
    def __str__(self):
        return str(self.boundaries)
    
    def fill(self, boundaries):
        for key in self.limits:
            self.boundaries[key] = []
            if key in boundaries:
                for seg in boundaries[key]:
                    if seg[1] < self.limits[key][0]: continue
                    if seg[0] > self.limits[key][1]: continue
                    mi = max(self.limits[key][0], seg[0])
                    ma = min(self.limits[key][1], seg[1])
                    self.boundaries[key].append([mi, ma])
            if len(self.boundaries[key]) == 0:
                self.boundaries[key] = [self.limits[key]]
    
    def intersect_1d(self, key, segs):
        ans = []
        i = j = 0
        while i < len(self.boundaries[key]) and j < len(segs):
            lo = max(self.boundaries[key][i][0], segs[j][0])
            hi = min(self.boundaries[key][i][1], segs[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            if self.boundaries[key][i][1] < segs[j][1]:
                i += 1
            else:
                j += 1
        return ans
    
    def union_1d(self, key, segs):
        unions = []
        i = j = 0
        while i < len(self.boundaries[key]) and j < len(segs):
            lo = min(self.boundaries[key][i][0], segs[j][0])
            hi = max(self.boundaries[key][i][1], segs[j][1])
            if lo <= hi:
                unions.append([lo, hi])
            if self.boundaries[key][i][1] < segs[j][1]:
                i += 1
            else:
                j += 1
        
        ans = []
        if len(unions) > 0:
            lo = unions[0][0]
            for i in range(len(unions) - 1):
                if unions[i][1] < unions[i + 1][0]:
                    ans.append([lo, unions[i][1]])
                    lo = unions[i + 1][0]
            ans.append([lo, unions[-1][1]])
        return ans
    
    def complement_1d(self, key):
        ans = []
        lo, hi = self.limits[key]
        for start, end in self.boundaries[key]:
            if lo < start:
                ans.append([lo, start - 1])
            lo = end + 1
        if lo <= hi:
            ans.append([lo, hi])
        return ans

    def subtract_1d(self, key, other):
        return self.intersect_1d(key, other.complement_1d(key))

    def intersect(self, other, key = None):
        if key:
            self.boundaries[key] = self.intersect_1d(key, other.boundaries[key])
        else:
            for key in other.boundaries:
                self.boundaries[key] = self.intersect_1d(key, other.boundaries[key])
    
    def union(self, other, key = None):
        if key:
            self.boundaries[key] = self.union_1d(key, other.boundaries[key])
        else:
            for key in other.boundaries:
                self.boundaries[key] = self.union_1d(key, other.boundaries[key])
    
    def complement(self, key = None):
        if key:
            self.boundaries[key] = self.complement_1d(key)
        else:
            for key in self.boundaries:
                self.boundaries[key] = self.complement_1d(key)
    
    def subtract(self, other, key = None):
        if key:
            self.boundaries[key] = self.subtract_1d(key, other)
        else:
            for key in other.boundaries:
                self.boundaries[key] = self.subtract_1d(key, other)
    
    def cap(self, min_caps, max_caps):
        for key in min_caps:
            self.boundaries[key] = self.intersect_1d(key, [[min_caps[key], self.limits[key][1]]])
        for key in max_caps:
            self.boundaries[key] = self.intersect_1d(key, [[self.limits[key][0], max_caps[key]]])
    
    def extend(self, min_extend, max_extend):
        for key in min_extend:
            self.boundaries[key] = self.union_1d(key, [[min_extend[key], self.limits[key][1]]])
        for key in max_extend:
            self.boundaries[key] = self.union_1d(key, [[self.limits[key][0], max_extend[key]]])
    
    def combinations(self):
        result = 1
        for key in self.boundaries:
            for seg in self.boundaries[key]:
                result *= (seg[1] - seg[0] + 1)
        return result

def get_workflows():
    w = l[0].split('\n')
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

def get_intervals():
    workflows = get_workflows()
    intervals = {}
    for workflow in workflows:
        intervals[workflow] = []
        current = Interval()
        for instruction in workflows[workflow]:
            if len(instruction) == 1:
                intervals[workflow].append((current, instruction[0]))
            else:
                key, thres, left, ret = instruction
                interval = Interval(current.boundaries)
                if left < 0:
                    interval.cap({}, {key: thres - 1})
                else:
                    interval.cap({key: thres + 1}, {})
                intervals[workflow].append((interval, ret))
                current.subtract(interval, key)
    return intervals

def solution():
    intervals = get_intervals()
    queue = [('in', intervals['in'], Interval())]
    visited = set()
    leafs = []
    while queue:
        name, workflow, interval = queue.pop()
        visited.add(name)
        for new_interval, key in workflow[::-1]:
            new_interval.intersect(interval)
            if key in visited: continue
            if key not in  ('A', 'R'):
                queue.append((key, intervals[key], new_interval))
            elif key == 'A':
                leafs.append(new_interval)
    
    result = sum(interval.combinations() for interval in leafs)
    return  result

result = solution()

print(result)