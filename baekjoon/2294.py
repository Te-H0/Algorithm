import sys

INF = int(1e9)
n, k = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]
dp = [INF] * (100000 + 1)
for l in li:
    dp[l] = 1

for l in li:
    for i in range(l, k + 1):
        dp[i] = min(dp[i], dp[l] + dp[i - l])
if dp[k] == INF:
    dp[k] = -1
print(dp[k])
