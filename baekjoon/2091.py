import sys

x, a, b, c, d = map(int, sys.stdin.readline().split())

dp = [[0, 0, 0, 0] for _ in range(x + 1)]
total = [0] * (x + 1)
for i in range(1, x + 1):
    if dp[i - 1][0] + 1 <= a:
        if i == 1 or total[i - 1] != 0:
            dp[i] = dp[i - 1][:]
            dp[i][0] += 1
            total[i] = total[i - 1] + 1
    if (i == 5 and dp[i - 5][1] + 1 <= b) or (
        i - 5 > 0 and total[i - 5] != 0 and dp[i - 5][1] + 1 <= b
    ):
        if total[i - 5] + 1 > total[i]:
            dp[i] = dp[i - 5][:]
            dp[i][1] += 1
            total[i] = total[i - 5] + 1
    if (i == 10 and dp[i - 5][2] + 1 <= c) or (
        i - 10 > 0 and total[i - 10] != 0 and dp[i - 10][2] + 1 <= c
    ):
        if total[i - 10] + 1 > total[i]:
            dp[i] = dp[i - 10][:]
            dp[i][2] += 1
            total[i] = total[i - 10] + 1
    if (i == 25 and dp[i - 5][3] + 1 <= d) or (
        i - 25 > 0 and total[i - 25] != 0 and dp[i - 25][3] + 1 <= d
    ):
        if total[i - 25] + 1 > total[i]:
            dp[i] = dp[i - 25][:]
            dp[i][3] += 1
            total[i] = total[i - 25] + 1

if total[x] == 0:
    for _ in range(4):
        print(0, end=" ")
else:
    for d in dp[x]:
        print(d, end=" ")
