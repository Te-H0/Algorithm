import heapq
import sys
n, m, k, x = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[] for i in range(n+1)]
dist = [INF] * (n+1)
ans=[]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((1, b))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue

        for i in graph[now]:
            cost = d + 1
            if dist[i[1]] > cost:
                dist[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


dijkstra(x)

for i in range(1,n+1):
    if dist[i] == k:
        ans.append(i)

if not ans:
    print(-1)
else:
    for i in ans:
        print(i)
