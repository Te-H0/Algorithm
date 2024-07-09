import sys
from collections import deque


def dfs(idx, cnt):
    if cnt == 6:
        print(*dq)
        return

    for i in range(idx, k):
        dq.append(s[i])
        dfs(i + 1, cnt + 1)
        dq.pop()


while True:
    l = list(map(int, sys.stdin.readline().split()))
    k = l[0]

    if k == 0:
        break
    s = l[1:]

    dq = deque()
    dfs(0, 0)
    print()
