import sys
INF = -int(1e9)
move = [(1, 0), (0, 1), (0, -1)]
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp=[[INF] * (m+2) for _ in range(n+2)]
dp[1][1] = graph[0][0]

# 첫째줄은 1,1에서 시작해야해서 오른쪽 -> 왼쪽 없다
for i in range(2,m+1):
    dp[1][i] = dp[1][i-1] + graph[0][i-1]
    
for i in range(2,n+1):
    left = [INF] * (m+2)
    right = [INF] * (m+2)
    
    # 왼 -> 오
    for j in range(1,m+1):
        left[j] = max(dp[i-1][j],left[j-1]) + graph[i-1][j-1]
    # 오 -> 왼
    for j in range(m,0,-1):
        right[j] = max(dp[i-1][j],right[j+1]) + graph[i-1][j-1]
    
    for j in range(1,m+1):
        dp[i][j] = max(left[j],right[j])
print(dp[n][m])
