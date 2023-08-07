import sys

f = sys.stdin.readline

n, m = map(int, f().split())

l = list(map(int, f().split()))

multi = [0]*(n+1)
check_multi = [0]*(n+1)
multi[0] = -1
check_multi[0] = -1
cnt = 0

for i in range(m):
    if l[i] in multi:
        continue

    if 0 in multi:
        idx = multi.index(0)
        multi[idx] = l[i]

    else:
        if i == m-1:
            cnt += 1
            continue

        for j in range(1, n+1):
            check_multi[j] = l[i+1:].count(multi[j])
        if 0 in check_multi:
            multi[check_multi.index(0)] = l[i]
            cnt += 1

        else:
            for j in range(1, n+1):
                check_multi[j] = l[i+1:].index(multi[j])

            tmp = max(check_multi)
            idx = check_multi.index(tmp)
            multi[idx] = l[i]
            cnt += 1

print(cnt)

