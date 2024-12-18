import sys

n, k = map(int, sys.stdin.readline().split())
dp= [0] * (k+1)
dp[0] = 1
li = [int(sys.stdin.readline()) for _ in range(n)]

for l in li:
    for i in range(l,k+1):
        dp[i] += dp[i-l]

print(dp[-1])