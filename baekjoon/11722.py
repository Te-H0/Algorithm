import sys

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))
dp = [1] * n


for i in range(n):
    for j in range(i):
        if li[i] < li[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))