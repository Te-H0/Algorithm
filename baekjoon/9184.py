import sys

dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a> 20 or b>20 or c>20:
        return w(20,20,20)
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    if a<b and b<c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]
while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a== -1 and b== -1 and c== -1:
        break
    print(f'w{a,b,c} = {w(a,b,c)}')
    
        
    # a,b,c 중 0이하인거있으면 1
    # a,b,c 중 20 초과인거있으면 W(20,20,20)
    # 1~19
    # a,b,c가 오름차순이면 w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    # 아니면  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)