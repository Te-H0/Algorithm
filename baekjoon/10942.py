import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

dp = [[0] * n for _ in range(n)]

for j in range(n):
    i = 0
    while j < n:
        if i == j:
            dp[i][j] = 1
        elif i + 1 == j:
            if l[i] == l[j]:
                dp[i][j] = 1
        else:
            if l[i] == l[j]:
                if dp[i + 1][j - 1]:
                    dp[i][j] = 1
        i += 1
        j += 1

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])
