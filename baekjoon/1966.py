import sys
from collections import deque
from queue import PriorityQueue

t = int(sys.stdin.readline())
answer = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    prior = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        answer.append(1)
        continue

    pq = PriorityQueue()
    for idx in range(n):
        pq.put(-prior[idx])

    dq = deque()
    for idx in range(n):
        dq.append((prior[idx], idx))

    cnt = 0
    while not pq.empty():
        cnt += 1
        p = -pq.get()
        pri, i = dq.popleft()
        while pri != p:
            dq.append((pri, i))
            pri, i = dq.popleft()
        if i == m:
            answer.append(cnt)
            break
for a in answer:
    print(a)
