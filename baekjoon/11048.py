import sys
move = [(-1, 0), (0, -1), (-1, -1)]
n, m = map(int, sys.stdin.readline().split())

l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = l[0][0]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        for m_i, m_j in move:
            n_i = i + m_i
            n_j = j + m_j

            if n_i in range(n) and n_j in range(m):
                dp[i][j] = max(dp[i][j], dp[n_i][n_j] + l[i][j])

print(dp[n-1][m-1])
