import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
dp= li[:]
dp[0] = li[0]

for i in range(1, n):
    for j in range(i):
        if li[j] < li[i]:
            dp[i] = max(dp[i], dp[j] + li[i])
print(max(dp))
