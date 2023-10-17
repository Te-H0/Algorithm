import sys
from collections import deque
n, l = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))
dq = deque()
for idx, x in enumerate(li):
    while dq and dq[-1][0] > x:
        dq.pop()
    while dq and dq[0][1] < idx - l + 2:  # idx +1 - l + 1
        dq.popleft()
    dq.append((x, idx+1))
    print(dq[0][0], end=" ")
