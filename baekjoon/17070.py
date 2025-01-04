import sys
from collections import deque

type = (0, 1, 2)  # 가로, 세로, 대각선
move = [
    [(0, 1), (1, 1)],
    [(1, 0), (1, 1)],
    [(0, 1), (1, 0), (1, 1)],
]  # 가로, 세로, 대각선
n = int(sys.stdin.readline())

li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 가로, 세로, 대각선
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
for i in range(n):
    for j in range(n):
        for k in range(3):
            # 가로상태
            if k ==0:
                # 옆으로 밀기
                if j+1 < n and li[i][j+1] == 0:
                    dp[k][i][j+1] += dp[k][i][j]
                # 대각선으로 밀기
                if i+1 <n and j+1 <n and li[i][j+1] + li[i+1][j+1] + li[i+1][j] ==0:
                    dp[2][i+1][j+1] += dp[k][i][j]
            # 세로 상태
            if k ==1 :
                # 아래로 밀기
                if i+1 < n and li[i+1][j] == 0:
                    dp[k][i+1][j] += dp[k][i][j]
                # 대각선으로 밀기
                if i+1 <n and j+1 <n and li[i][j+1] + li[i+1][j+1] + li[i+1][j] ==0:
                    dp[2][i+1][j+1] += dp[k][i][j]
            if k==2:
                # 옆으로 밀기
                if j+1 < n and li[i][j+1] == 0:
                    dp[0][i][j+1] += dp[k][i][j]
                 # 아래로 밀기
                if i+1 < n and li[i+1][j] == 0:
                    # print(i,j,k)
                    dp[1][i+1][j] += dp[k][i][j]
                # 대각선으로 밀기
                if i+1 <n and j+1 <n and li[i][j+1] + li[i+1][j+1] + li[i+1][j] ==0:
                    dp[k][i+1][j+1] += dp[k][i][j]

# print(*dp[0])
# print(*dp[1])
# print(*dp[2])
# print(dp[0][n-1][n-1], dp[1][n-1][n-1], dp[2][n-1][n-1])
print(dp[0][n-1][n-1]+ dp[1][n-1][n-1]+ dp[2][n-1][n-1])