import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline()) - 1  # 시작 지점
INF = int(1e9)
distance = [INF] * v
graph = [[] for _ in range(v)]
for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())

    graph[u-1].append((v-1, w))
dijkstra(k)

for d in distance:
    if d == INF:
        print("INF",end=' ')
    else:
        print(d,end=' ')
