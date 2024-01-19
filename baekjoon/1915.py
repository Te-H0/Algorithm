import sys

n, m = map(int, sys.stdin.readline().split())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip())))
dp = [[0] * m for _ in range(n)]


for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 or li[i][j] == 0:
            dp[i][j] = li[i][j]

        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
result = 0
for p in dp:
    result = max(result,max(p))
print(result **2)
