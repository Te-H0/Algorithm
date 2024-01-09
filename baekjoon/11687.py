import sys, math

m = int(sys.stdin.readline())
answer = int(1e9)


def count_zero(x):
    cnt = 0

    while x >= 5:
        cnt += x // 5
        x = x // 5
    return cnt


left, right, mid = 1, m * 5, (1 + m * 5) // 2

while left <= right:
    tmp = count_zero(mid)

    if tmp < m:
        left = mid + 1
    else:
        right = mid - 1

    if m == tmp:
        answer = mid

    mid = (left + right) // 2

if answer != int(1e9):
    print(answer)
else:
    print(-1)
