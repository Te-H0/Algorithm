import sys

t = int(sys.stdin.readline())
case = [int(sys.stdin.readline()) for _ in range(t)]
m = max(case)
dp = [1] * (m + 1)

for i in range(2, m + 1):
    dp[i] += dp[i - 2]

for i in range(3, m + 1):
    dp[i] += dp[i - 3]

for c in case:
    print(dp[c])
