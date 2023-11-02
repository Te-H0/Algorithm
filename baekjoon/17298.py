import sys
from collections import deque
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
dq = deque()
dq_idx = deque()
answer = [-1]*n

for i in range(n):
    now = l[i]
    while dq and dq[0] < now:
        dq.popleft()
        answer[dq_idx.popleft()] = now

    dq.appendleft(now)
    dq_idx.appendleft(i)

for i in answer:
    print(i,end=' ')
