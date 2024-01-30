import sys

t = int(sys.stdin.readline())
dp = [0] * 100

for i in range(1, 100):
    if 1 <= i <= 9:
        dp[i] = dp[i-1]+1
    elif 10 <= i <= 24:
        dp[i] = min(dp[i - 1], dp[i - 10]) + 1
    else:
        dp[i] = min(dp[i - 1], dp[i - 10], dp[i - 25]) + 1

for _ in range(t):
    x = int(sys.stdin.readline())

    answer = 0

    while x != 0:
        answer += dp[x % 100]
        x //= 100
    print(answer)
