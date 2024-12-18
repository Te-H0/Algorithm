import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li2 = li[::-1]
dp = [1] * n
dp2 = [1] * n

for i in range(1, n):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(1, n):
    for j in range(i):
        if li2[i] > li2[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2 = dp2[::-1]
answer = 0

for i in range(n):
    answer = max(answer, dp[i] + dp2[i] - 1)

print(answer)