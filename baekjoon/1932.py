import sys
n = int(sys.stdin.readline())

dp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if i == 0 and j == 0:
            continue
        elif j == 0:
            dp[i][j] += dp[i-1][j]
        elif i == j:
            dp[i][j] += dp[i-1][j-1]

        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
