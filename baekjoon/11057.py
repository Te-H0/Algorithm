import sys

n = int(sys.stdin.readline())
dp = [[0]*(10) for _ in range(n+1)]

dp[0][0] = 1

for i in range(1, n+1):
    for j in range(10):
        if dp[i-1][j] != 0:
            for k in range(j, 10):
                dp[i][k] += dp[i-1][j]

print(sum(dp[n])%10007)
