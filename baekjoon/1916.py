import sys
import heapq
INF=int(1e9)

n = int(sys.stdin.readline()) # 도시 개수
m = int(sys.stdin.readline()) # 버스 수
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
for _ in range(m):
    start, end, cost = map(int,sys.stdin.readline().split())
    graph[start].append((end,cost))
    
start, end = map(int,sys.stdin.readline().split())

def dijkstra(start):
    q=[]
    heapq.heappush(q,(start,0))
    dist[start] = 0
    
    while q:
        city,cost =heapq.heappop(q)
        if dist[city] < cost:
            continue
        
        for g in graph[city]:
            c = cost + g[1]
            if c < dist[g[0]]:
                dist[g[0]] = c
                heapq.heappush(q,(g[0],c))
                
dijkstra(start)
print(dist[end])
    
    
    
