import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
l = [False] * 100001


def bfs():
    cnt = 0
    dq = deque()
    dq.append((n, 0))
    l[n] = True
    while dq:
        x, cnt = dq.popleft()

        if x == k:
            return cnt

        a = x-1
        b = x+1
        c = 2*x

        if 0 <= c <= 100000 and l[c] == False:
            dq.append((c, cnt))
            l[c] = True
        if 0 <= a <= 100000 and l[a] == False:
            dq.append((a, cnt+1))
            l[a] = True
        if 0 <= b <= 100000 and l[b] == False:
            dq.append((b, cnt+1))
            l[b] = True


print(bfs())
