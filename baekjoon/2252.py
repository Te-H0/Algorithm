import sys
from collections import deque
f = sys.stdin.readline

n, m = map(int, f().split())

graph = [[]for i in range(n+1)]
indegree = [0]*(n+1)
answer = []

for i in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    dq = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            dq.append(i)
            answer.append(i)

    while dq:
        x = dq.popleft()

        for i in graph[x]:
            indegree[i] -= 1

            if indegree[i] == 0:
                dq.append(i)
                answer.append(i)


topology_sort()

for i in answer:
    print(i, end=' ')
