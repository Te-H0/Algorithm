import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
answer = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]


def topology_sort():
    flag = False
    dq = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            dq.append((i,1))
    

    while dq:
        x,cnt = dq.popleft()
        answer[x] = cnt
        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                dq.append((i,cnt+1))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort()

print(*answer[1:])
