import sys 

n= int(sys.stdin.readline())

l = list(map(int,input().split()))

dp=[1]*n

for i in range(1,n):
    tmp=1
    for j in range(i):
        if l[i]>l[j]:
            tmp = max(tmp,dp[j]+1)
    dp[i]=tmp
    

print(max(dp))
