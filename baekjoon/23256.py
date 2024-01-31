import sys

t = int(sys.stdin.readline())
li=[2,2,1,2] # 왼,오,둘다,안돼
l_dp = [0] * 1000001
l_dp[1] = 3
r_dp = [0] * 1000001
r_dp[1] = 4

for i in range(2, 1000001):
    l_dp[i] = (l_dp[i-1]*(li[1]+li[2]) + r_dp[i-1]*(li[2]))% 1000000007
    r_dp[i] = (l_dp[i-1]*(li[3]+li[0]) + r_dp[i-1]*(li[0]))% 1000000007

for _ in range(t):
    n = int(sys.stdin.readline())
    print((l_dp[n] + r_dp[n]) % 1000000007)
