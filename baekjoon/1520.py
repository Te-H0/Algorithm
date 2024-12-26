import sys
sys.setrecursionlimit(10**9)

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, sys.stdin.readline().split())

li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for m_x, m_y in move:
            n_x = x + m_x
            n_y = y + m_y
            if (0 <= n_x < n and 0 <= n_y < m) and li[x][y] > li[n_x][n_y]:
                dp[x][y] += dfs(n_x, n_y)
    return dp[x][y]

print(dfs(0, 0))
