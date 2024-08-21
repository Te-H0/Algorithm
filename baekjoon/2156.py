import sys

n = int(sys.stdin.readline())
li = [0]
for _ in range(n):
    li.append(int(sys.stdin.readline()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[i] = li[i]
    elif i == 2:
        dp[i] = dp[i - 1] + li[i]
    else:
        # 1. 본인포함 연속 + 3개전 총합 2. 본인 앞에꺼 안먹고 본인 포함 3. 본인 제외
        dp[i] = max(dp[i - 3] + li[i - 1] + li[i], dp[i - 2] + li[i], dp[i - 1])

print(dp[n])
