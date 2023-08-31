import heapq
import sys

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())

graph = [[]for _ in range(n+1)]

dist = [INF] * (n+1)
dist[1] = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(graph)


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        di, now = heapq.heappop(q)
        print(di, now)
        if dist[now] < di:
            continue
        for i in graph[now]:
            cost = di + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra()
print(dist[n])
