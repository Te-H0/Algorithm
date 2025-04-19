import sys
import heapq

INF = int(1e9)
t = int(sys.stdin.readline())


def dijkstra(x):
    dist[x] = 0
    q = []
    heapq.heappush(q, (0, x))

    while q:
        di, a = heapq.heappop(q)
        if dist[a] < di:
            continue

        for n_x, cost in graph[a]:
            if dist[n_x] > cost + di:
                dist[n_x] = cost + di
                heapq.heappush(q, (cost + di, n_x))


for _ in range(t):
    # 컴퓨터 수, 의존성 수, 해킹 컴퓨터
    n, d, c = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n)]
    dist = [INF] * n
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b - 1].append((a - 1, s))

    dijkstra(c - 1)
    total_cnt = n - dist.count(INF)
    result = set(dist)
    if INF in result:
        result.remove(INF)

    print(n - dist.count(INF), max(result))