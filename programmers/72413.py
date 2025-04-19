import heapq
from collections import defaultdict
INF = int(1e9)
def dijkstra(n, start, graph):
    dist = [INF] * n
    q = [(start,0)]
    dist[start] = 0
    while q:
        # [(s,a), (s,b),(a,b),(b,a)]
        # print(dist)
        node , di = heapq.heappop(q)
        
        if dist[node] < di:
            continue
            
        for x, c in graph[node]:
            cost = di + c
            if dist[x] > cost:
                
                dist[x] = cost
                heapq.heappush(q,(x, cost))
    return dist

def solution(n, s, a, b, fares):
# 함께 갈 때 -> s,a,b / s,b,a
# 따로 갈 때 -> s,a + s,b
# 구해야할 것 s -> a / s -> b / a -> b / b -> a
    answer = INF
    di = defaultdict(int)
    graph = [[] for _ in range(n)]
    
    for c,d,f in fares:
        graph[c-1].append((d-1,f))
        graph[d-1].append((c-1,f))
    
    D = [dijkstra(n, i, graph) for i in range(n)]
        
    for i in range(n):
        answer = min(answer, D[s-1][i] + D[i][a-1] + D[i][b-1])
    return answer