import sys

# 지각 2번이상, 3연속 결석
MOD = 1000000
n = int(sys.stdin.readline())

dp = [[[0] * (3) for _ in range(2)] for _ in range(n + 1)]
# 날짜, 지각, 결석
dp[1][0][0], dp[1][0][1], dp[1][1][0] = 1, 1, 1

for i in range(2, n + 1):
    dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % MOD

    dp[i][0][1] = dp[i - 1][0][0] % MOD

    dp[i][0][2] = dp[i - 1][0][1] % MOD

    dp[i][1][0] = (
        dp[i - 1][0][0]
        + dp[i - 1][0][1]
        + dp[i - 1][0][2]
        + dp[i - 1][1][0]
        + dp[i - 1][1][1]
        + dp[i - 1][1][2]
    ) % MOD

    dp[i][1][1] = dp[i - 1][1][0] % MOD

    dp[i][1][2] = dp[i - 1][1][1] % MOD

print(
    (dp[n][0][0] + dp[n][0][1] + dp[n][0][2] + dp[n][1][0] + dp[n][1][1] + dp[n][1][2])
    % MOD
)
