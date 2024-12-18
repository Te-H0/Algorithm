import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

dp=[0] + li[:]

for i in range(2, n + 1):
    k = round(i / 2) + 1
    for j in range(1, k):
        dp[i] = max(dp[i], dp[j] + dp[i - j])
print(dp[-1])

# 3 6 15 