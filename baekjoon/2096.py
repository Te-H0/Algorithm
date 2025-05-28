import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))


pre1 = li[0][:]
pre2 = li[0][:]
now1, now2 = [0] * 3, [0] * 3
for i in range(1, n):

    for j in range(3):
        tmp1, tmp2 = 0, 0
        if j == 0:
            tmp1 = max(pre1[:2])
            tmp2 = min(pre2[:2])
        elif j == 1:
            tmp1 = max(pre1[:])
            tmp2 = min(pre2[:])
        else:
            tmp1 = max(pre1[1:])
            tmp2 = min(pre2[1:])
        now1[j] = tmp1 + li[i][j]
        now2[j] = tmp2 + li[i][j]

    pre1 = now1[:]
    pre2 = now2[:]
print(max(now1), min(now2))

