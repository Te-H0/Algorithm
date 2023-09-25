import sys
from collections import deque
n = int(sys.stdin.readline())

map=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

goal = [[0]*n for _ in range(n)]
goal[0][0] = 1

for i in range(n):
    for j in range(n):
        if i== n - 1 and j==n-1:
            break

        if i + map[i][j] in range(n):
            goal[i+map[i][j]][j] += goal[i][j]
        
        if j + map[i][j] in range(n):
            goal[i][j+map[i][j]] += goal[i][j]

print(goal[n-1][n-1])



