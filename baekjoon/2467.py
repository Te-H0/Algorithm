import sys
INF = int(1e9)
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

s = 0
e = n-1

ans_left = 0
ans_right = n-1
total = abs(l[ans_left] + l[ans_right])

while s < e:
    tmp = l[s] + l[e]

    if total > abs(tmp):

        total = abs(tmp)
        ans_left = s
        ans_right = e

        if tmp == 0:
            break

    if tmp > 0:
        e -= 1
    else:
        s += 1

print(l[ans_left], l[ans_right])
