import sys
from collections import defaultdict


def init(n):
    di[1] = [n, 2]
    di[n] = [n - 1, 1]
    for i in range(2, n):
        di[i] = [i - 1, i + 1]


def delete(x):
    di[di[x][0]][1] = di[x][1]
    di[di[x][1]][0] = di[x][0]
    di.pop(x)


n, k = map(int, sys.stdin.readline().split())
if n == 1:
    print("<1>")
else:
    di = defaultdict(list)
    init(n)
    answer = []
    x = 1
    while len(di) != 0:
        for i in range(k - 1):
            x = di[x][1]
        next = di[x][1]
        delete(x)
        answer.append(str(x))
        x = next

    print("<" + ", ".join((answer)) + ">")