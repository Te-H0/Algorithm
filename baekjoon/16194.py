import sys

n = int(sys.stdin.readline())

dp = [0]
dp.extend(list(map(int, sys.stdin.readline().split())))

for i in range(2, n+1):
    j = 1
    k = i-1
    while j <= k:
        dp[i] = min(dp[j]+dp[k], dp[i])
        j += 1
        k -= 1

print(dp[n])
