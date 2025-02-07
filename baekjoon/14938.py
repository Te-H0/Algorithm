import sys
import heapq

INF = int(1e9)
# n 지역, m 수색범위, r 길의 수
n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n)]
answer = 0

for i in range(r):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s - 1].append((c, e - 1))
    graph[e - 1].append((c, s - 1))

for i in range(n):
    dist = [INF] * n
    dist[i] = 0

    q = [(0, i)]
    while q:
        di, now = heapq.heappop(q)

        if dist[now] < di:
            continue

        for g in graph[now]:
            cost = g[0] + di
            node = g[1]

            if cost < dist[g[1]]:
                dist[node] = cost
                heapq.heappush(q, (cost, node))

    tmp = 0    
    for j in range(n):
        if dist[j] <= m:
            tmp += items[j]

    answer = max(answer, tmp)

print(answer)
