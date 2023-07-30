import sys
from collections import deque
f = sys.stdin.readline

m, n, k = map(int, f().split())
ans = []
l = [[1]*n for i in range(m)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(a, b):
    dq = deque()

    l[a][b] = 0
    cnt = 1
    dq.append((a, b))
    while dq:
        x = dq.popleft()
        for i in range(4):
            if x[0]+move[i][0] >= 0 and x[0]+move[i][0] < m and x[1]+move[i][1] >=0 and x[1]+move[i][1] < n and l[x[0]+move[i][0]][x[1]+move[i][1]] == 1:
                l[x[0]+move[i][0]][x[1]+move[i][1]] = 0
          
                dq.append((x[0]+move[i][0], x[1]+move[i][1]))
                cnt += 1
    return cnt


for i in range(k):
    a, b, c, d = map(int, f().split())
    for j in range(b, d):
        for k in range(a, c):
            l[j][k] = 0


for i in range(m):
    for j in range(n):
        if l[i][j] == 1:
            ans.append(bfs(i, j))

ans.sort()           
print(len(ans))
for i in ans:
    print(i,end=" ")

