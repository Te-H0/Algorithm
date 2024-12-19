import sys

n = int(sys.stdin.readline())
dp = [x for x in range(n+1)]

for i in range(1, n + 1):
    for j in range(1,i):
        if j*j > i:
            break
        elif dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1
            
print(dp[-1])