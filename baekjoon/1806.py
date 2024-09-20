import sys

n, s = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)
dp[1] = li[0]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + li[i - 1]

left = 0
right = 1
answer = n + 1

for i in li:
    if i >= s:
        answer = 1
    break

while left <= right and right <= n and answer != 1:

    if dp[right] - dp[left] >= s:
        answer = min(answer, right - left)
        left += 1
    else:
        right += 1
if answer == n + 1:
    answer = 0
print(answer)
