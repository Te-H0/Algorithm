import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
l = [0]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    l.append((a, b))
k = int(sys.stdin.readline())
if n == 1:
    print(0)
else:
    dp[2] = l[1][0]
    for i in range(3, n + 1):
        dp[i] = min(dp[i - 1] + l[i - 1][0], dp[i - 2] + l[i - 2][1])
    answer = dp[n]
    for i in range(1, n - 2):
    
        dp2 = [0] * (n + 1)
        dp[2] = l[1][0]
        dp2[i + 3] = dp[i] + k

        if i + 4 < n + 1:
            dp2[i + 4] = dp2[i + 3] + l[i + 3][0]
        for j in range(i + 5, n + 1):
            dp2[j] = min(dp2[j - 1] + l[j - 1][0], dp2[j - 2] + l[j - 2][1])
        answer = min(answer,dp2[n])
        
    print(answer)
