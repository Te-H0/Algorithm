import sys

n = int(sys.stdin.readline())
cost=[list(map(int,sys.stdin.readline().split())) for _ in range(n)] # R, G, B 순서
dp = [[0,0,0] for _ in range(n)] # R, G, B 순서 - i번째에서 각각 R, G, B를 선택한 값
dp[0] = cost[0][:]

for i in range(1,n):
    #R을 선택한 경우
    dp[i][0] = min(dp[i-1][1], dp[i-1][2] )+ cost[i][0]
    
    #G를 선택한 경우
    dp[i][1] = min(dp[i-1][0], dp[i-1][2])+ cost[i][1]
    
    #B를 선택한 경우
    dp[i][2] = min(dp[i-1][0], dp[i-1][1] ) + cost[i][2]
    
print(min(dp[n-1]))