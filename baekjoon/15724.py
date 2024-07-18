import sys

n, m = map(int, sys.stdin.readline().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = l[i-1][j-1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

k = int(sys.stdin.readline())

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(answer)
