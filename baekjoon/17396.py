import sys
import heapq

INF = int(1e50)
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li[-1] = 0

graph = [[] for _ in range(n)]
dist = [INF] * n
for _ in range(m):
    a, b, t = list(map(int, sys.stdin.readline().split()))
    graph[a].append((b, t))
    graph[b].append((a, t))


def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    dist[0] = 0

    while q:
        x, di = heapq.heappop(q)

        if dist[x] < di:
            continue
        for e, c in graph[x]:
            cost = di + c
            if dist[e] > cost and li[e] == 0:
                dist[e] = cost
                heapq.heappush(q, (e, cost))


dijkstra()
# print(dist)
if dist[-1] == INF:
    print(-1)
else:
    print(dist[-1])

