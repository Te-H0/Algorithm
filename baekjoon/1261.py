import sys
import heapq

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())

graph = []
penalty = 5000
for _ in range(m):
    x = sys.stdin.readline().strip()
    graph.append(list(map(int, x)))

dist = [[INF] * n for _ in range(m)]
dist[0][0] = 0
q = []
heapq.heappush(q, (0, 0, 0))

while q:
    cost, i, j = heapq.heappop(q)
    print(i, j)
    if dist[i][j] < cost:
        continue

    if i == m - 1 and j == n - 1:
        # print(cost)
        print(cost // penalty)
        break
    for m_i, m_j in move:
        n_i = i + m_i
        n_j = j + m_j

        if n_i in range(m) and n_j in range(n):
            n_cost = 1
            if graph[n_i][n_j] == 1:
                n_cost = penalty
            n_cost += cost 
            if dist[n_i][n_j] > n_cost:
                dist[n_i][n_j] = n_cost
                heapq.heappush(q, (n_cost, n_i, n_j))
# print(dist)