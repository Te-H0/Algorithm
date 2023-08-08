import sys
from collections import deque
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

graph=[]
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))


distance = 0


def bfs(i, j):
    check = [[0]*m for i in range(n)]
    dq = deque()
    dq.append((0, i, j))
    check[i][j] = 1
    ans = 0
    while dq:

        d, a, b = dq.popleft()

        for i in range(4):
            nx=a+move[i][0]
            ny=b+move[i][1]
            if 0<=nx<n and 0<= ny <m and  graph[nx][ny] == 'L' and check[nx][ny] == 0:
                dq.append((d+1, nx,ny))
                check[nx][ny] = 1
                ans = max(ans,d+1 )

    return ans

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            distance= max(distance,bfs(i, j))

print(distance)

