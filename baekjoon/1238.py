import sys, heapq

INF = int(1e9)
n, m, x = map(int, sys.stdin.readline().split())
answer = 0
start_graph = [[] for _ in range(n)]
graph = [[] for _ in range(n)]


def dijkstra(start, graph):
    q = []
    dist = [INF] * n
    dist[start] = 0
    heapq.heappush(q, (start, 0))
    while q:
        now, di = heapq.heappop(q)
        if di > dist[now]:
            continue
        for e, c in graph[now]:
            cost = di + c
            if cost < dist[e]:
                dist[e] = cost
                heapq.heappush(q, (e, cost))
    return dist


for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start - 1].append((end - 1, cost))
    start_graph[end - 1].append((start - 1, cost))

start_dist = dijkstra(x - 1, start_graph)
end_dist = dijkstra(x - 1, graph)
for i in range(n):
    answer = max(start_dist[i] + end_dist[i], answer)
print(answer)
