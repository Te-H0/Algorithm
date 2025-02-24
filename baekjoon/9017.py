import sys
from collections import defaultdict
from bisect import bisect, bisect_left

t = int(sys.stdin.readline())

for _ in range(t):
    di = defaultdict(list)

    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    point = 1
    tmp = li[:]
    tmp.sort()
    x = max(tmp)
    s = set()

    for i in range(1, x + 1):
        if bisect(tmp, i) - bisect_left(tmp, i) == 6:
            s.add(i)

    for l in li:
        if l in s:
            di[l].append(point)
            point += 1
    tmp = []
    for x in list(di.items()):
        tmp.append((x[0], sum(x[1][:4]), x[1][4]))
    tmp.sort(key=lambda x: [x[1], x[2]])
    print(tmp[0][0])
