import sys

n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
li.sort()
print(li)
dp = [1] * n

for i in range(1,n):
    x = li[i][1]
    for j in range(i):
        y = li[j][1]
        if x>y:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))