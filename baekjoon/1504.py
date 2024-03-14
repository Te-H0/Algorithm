import sys, heapq

INF = int(1e9)
n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]  # (도착지, 비용)
path = []


def dijkstra(start, end):
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (start, 0))  # 노드, 비용

    while q:
        node, cost = heapq.heappop(q)
        if dist[node] < cost:
            continue

        for x, y in graph[node]:
            c = cost + y

            if c < dist[x]:
                dist[x] = c
                heapq.heappush(q, (x, c))
    return dist[end]


for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
target1, target2 = map(int, sys.stdin.readline().split())

path.append(dijkstra(1, target1) + dijkstra(target1, target2) + dijkstra(target2, n))
path.append(dijkstra(1, target2) + dijkstra(target2, target1) + dijkstra(target1, n))

answer = min(path)

if answer >= INF:
    print(-1)
else:
    print(answer)