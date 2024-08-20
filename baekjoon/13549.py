import sys
from collections import deque

INF = int(1e9)
n, k = map(int, sys.stdin.readline().split())
visit = [INF] * 100001
dq = deque()
dq.append((n, 0))
visit[n] = 0


while dq:
    # print(dq)
    x, t = dq.popleft()
    if x == k:
        answer = t
        while dq:
            x2, t2 = dq.popleft()
            if x2 == k:
                answer = min(answer, t2)
        print(answer)
        break

    if 2 * x <= 100000 and visit[2 * x] > t:
        dq.append((2 * x, t))
        visit[2 * x] = t

    if x + 1 <= 100000 and visit[x + 1] > t+1:
        dq.append((x + 1, t + 1))
        visit[x + 1] = t+1

    if 0 <= x - 1 <= 100000 and  visit[x - 1] > t+1:
        dq.append((x - 1, t + 1))
        visit[x - 1] = t+1