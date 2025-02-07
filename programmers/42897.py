def solution(money):
    n = len(money)
    ans = list()
    dp = [0] * n
    dp[0] = money[0]
    dp[1] = money[0]

    # [0]을 무조건 포함할 경우
    for i in range(2, n - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    ans.append(dp[n - 2])

    # [n-1]을 무조건 포함할 경우
    dp = [0] * n
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    ans.append(dp[n - 1])

    print(ans)
    return max(ans)
