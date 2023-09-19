import sys,heapq
move=[(-1,0),(1,0),(0,-1),(0,1)]
def dijkstra(distance):
    q=[]
    heapq.heappush(q,(distance[0][0],0,0))

    while q:
        dist, i,j = heapq.heappop(q)
        
        if dist > distance[i][j]:
            continue

        for m_i, m_j in move:
            n_i = i + m_i
            n_j = j + m_j

            if n_i in range(0,n) and n_j in range(0,n):
                cost = dist + li[n_i][n_j]
                if cost < distance[n_i][n_j]:
                    distance[n_i][n_j] = cost
                    heapq.heappush(q,(distance[n_i][n_j],n_i,n_j))


        


idx = 1
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    li = []
    for _ in range(n):
        li.append(list(map(int, sys.stdin.readline().split())))
    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = li[0][0]
    dijkstra(distance)
    print(f'Problem {idx}: {distance[n-1][n-1]}')
    idx += 1



