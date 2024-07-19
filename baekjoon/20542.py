import sys

n,m = map(int,sys.stdin.readline().split())
wrong_word = sys.stdin.readline().strip()
correct_word = sys.stdin.readline().strip()

dp = [[0]* (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][0] = i
for j in range(1,m+1):
    dp[0][j] = j
    
for i in range(1,n+1):
    for j in range(1,m+1):
        if (wrong_word[i-1] == correct_word[j-1]) or (wrong_word[i-1]== 'i' and correct_word[j-1] in ('j','l')) or (wrong_word[i-1]== 'v' and correct_word[j-1] =='w'):
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1

print(dp[n][m])
    