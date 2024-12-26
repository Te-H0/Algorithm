import sys
import heapq

INF = int(1e9)
n, d = map(int, sys.stdin.readline().split())
graph = [[(i+1,1)] for i in range(d+1)]
graph[d] = []
for _ in range(n):
    s, e, c = map(int, sys.stdin.readline().split())
    if 0<=s<d and 0<=e<=d:
        graph[s].append((e, c))

dist = [INF] * (d+1)
dist[0] = 0

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))

    while q:
        x, cost = heapq.heappop(q)

        if dist[x] < cost:
            continue
        for m_x, m_c in graph[x]:
            n_c = cost + m_c
            if n_c < dist[m_x]:
                dist[m_x] = n_c
                heapq.heappush(q,(m_x,n_c))

dijkstra()
print(dist[d])
