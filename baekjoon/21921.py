import sys

n, x = map(int, sys.stdin.readline().split())
li = [0]

li += list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)

for i in range(1, x):
    dp[i] = dp[i - 1] + li[i]

for i in range(x, n + 1):
    dp[i] = dp[i - 1] + li[i] - li[i - x]

answer = max(dp)
if answer == 0:
    print('SAD')
else:
    print(answer)
    print(dp.count(answer))
