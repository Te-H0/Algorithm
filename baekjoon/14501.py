import sys
import copy

n = int(sys.stdin.readline())

t = [-1]
p = [-1]

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = copy.deepcopy(p)

for i in range(1, n+1):
    for j in range(1, i):

        if (j+t[j] <= i):
            if i == 4:
                print('i>>>', i, 'j>>>>', j, 'pi>>>>', p[i], 'dp[j]+p[i]>>>', dp[j]+p[i])
            dp[i] = max(p[i], dp[j]+p[i])
        else:
            dp[i] = p[i]
    if i+t[i] > n+1:
        dp[i] = max(dp[:i])

print(dp)
