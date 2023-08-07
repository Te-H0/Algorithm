import sys
from collections import deque

n = int(sys.stdin.readline())
m=0
l = list(map(int, sys.stdin.readline().split()))
check = [False] * n


def sol(tmp_li):
    global m
    if len(tmp_li) == n:
        answer = 0
        for i in range(n-1):
            tmp = tmp_li[i]-tmp_li[i+1]
            if tmp < 0:
                tmp = tmp * -1
            answer += tmp
        if answer == 62:
            print(tmp_li)
        return answer

    for i in range(n):
        if not check[i]:
            tmp_li.append(l[i])
            check[i] = True
            m = max(m, sol(tmp_li))
            tmp_li.pop()
            check[i] = False

    return m


print(sol([]))
