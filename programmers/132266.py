import heapq
INF = int(1e9)
def dijkstra(start, graph, dist):
    q = [(start,0)]
    
    while q:
        x, cost = heapq.heappop(q)
        if dist[x] < cost:
            continue
        
        for m in graph[x]:
            n_c = cost + 1
            
            if n_c < dist[m]:
                dist[m] = n_c
                heapq.heappush(q,(m,n_c))
        
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for x,y in roads:
        graph[x].append(y)
        graph[y].append(x)
    dist = [INF] * (n+1)
    dist[destination] = 0
    dijkstra(destination, graph, dist)
    for s in sources:
        if dist[s] == INF:
            answer.append(-1)
        else:
            answer.append(dist[s])
        
    return answer