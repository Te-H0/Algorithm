import sys

n, m = map(int, sys.stdin.readline().split())
l = []
for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = l[0][0]

for i in range(n):
    for j in range(n):
        dp[i][j] = l[i][j]
        if i - 1 >= 0:
            dp[i][j] += dp[i-1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i][j-1]
        if i-1 >= 0 and j-1 >= 0:
            dp[i][j] -= dp[i-1][j-1]
for _ in range(m):
    tmp_x1, tmp_y1, tmp_x2, tmp_y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = tmp_x1-1, tmp_y1-1, tmp_x2-1, tmp_y2-1

    answer = dp[x2][y2]

    if x1-1 >= 0:
        answer -= dp[x1-1][y2]
    if y1-1 >= 0:
        answer -= dp[x2][y1-1]

    if x1 - 1 >= 0 and y1-1 >= 0:
        answer += dp[x1-1][y1-1]
    print(answer)

