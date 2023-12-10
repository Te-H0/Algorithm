import sys
from queue import PriorityQueue
from collections import deque

n, k, t = map(int, sys.stdin.readline().split())
shark = list(map(int, sys.stdin.readline().split()))
shark.sort()
dq = deque(shark)
cnt = 0
pq = PriorityQueue()

while cnt < k:
    while dq and dq[0] < t:
        x = dq.popleft()
        pq.put(-x)
    if not pq.empty():
        x = pq.get()
        x *= -1
        cnt += 1
        t += x
    else:
        break

print(t)
