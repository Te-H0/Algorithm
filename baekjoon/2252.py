import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
li = [[] for _ in range(n + 1)]  # 내가 앞서 나와야 하는 수들
indegree = [0] * (n + 1)
answer = []

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    li[x].append(y)
    indegree[y] += 1

dq = deque()
for i in range(1, n + 1):
    if not indegree[i]:
        dq.append(i)
        answer.append(i)

while dq:
    x = dq.popleft()

    for l in li[x]:
        indegree[l] -= 1

        if not indegree[l]:
            dq.append(l)
            answer.append(l)

print(*answer)