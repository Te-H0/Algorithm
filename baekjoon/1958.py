import sys

words = [sys.stdin.readline().rstrip() for _ in range(3)]
dp = [
    [[0] * (len(words[2]) + 1) for _ in range((len(words[1]) + 1))]
    for _ in range((len(words[0]) + 1))
]

for i in range(1, len(words[0]) + 1):
    for j in range(1, len(words[1]) + 1):
        for k in range(1, len(words[2]) + 1):
            if words[0][i-1] == words[1][j-1] == words[2][k-1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

print(dp[len(words[0])][len(words[1])][len(words[2])])
