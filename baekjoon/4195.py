import sys


def find(x):
    if l[x] < 0:
        return x

    l[x] = find(l[x])
    return l[x]


def union(x, y):
    x_p = find(x)
    y_p = find(y)
    
    if x_p < y_p:  # x가 대장
        l[x_p] += l[y_p]
        l[y_p] = x_p
        print(-l[x_p])
    elif x_p == y_p:
        print(x_p)
    else:
        l[y_p] += l[x_p]
        l[x_p] = y_p
        print(-l[y_p])


n = int(sys.stdin.readline())

for _ in range(n):
    f = int(sys.stdin.readline())
    l = [-1] * 200002

    di = dict()
    cnt = 1
    for _ in range(f):
        x, y = map(str, sys.stdin.readline().split())

        if x not in di:
            di[x] = cnt
            cnt += 1

        if y not in di:
            di[y] = cnt
            cnt += 1
        union(di[x], di[y])
