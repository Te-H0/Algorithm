import sys
import copy

n = int(sys.stdin.readline())

t = [-1]
p = [-1]

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp=[0]*(n+1)
if t[1]<=n:
    dp[1]=p[1]

for i in range(2,n+1):
    for j in range(1,i):
        if j+t[j]<=i:
            if i+t[i]<=n+1:
                dp[i]=max(dp[j]+p[i],dp[i])
        
    if (dp[i]==0) and (i+t[i]<=n+1):
        dp[i]=p[i]
        
print(max(dp))
