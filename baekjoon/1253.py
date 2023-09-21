from operator import truediv
import sys
from collections import deque
n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))
li.sort()
answer = 0


def sol(idx):
    l_point = 0
    r_point = n-1
    flag = False
    while l_point < r_point:
        if not flag:
            if l_point == idx:
                l_point += 1
                flag = True
                continue
            elif r_point == idx:
                r_point -= 1
                flag = True
                continue
        if li[l_point]+li[r_point] == li[idx]:
            return True
        elif li[l_point]+li[r_point] > li[idx]:
            r_point -= 1
        else:
            l_point += 1
    return False


for idx in range(n):
    if sol(idx):
        answer += 1
print(answer)

# 2

# 0 1

# out : 0

# 3

# 0 0 0

# out : 3

# 4

# 0 1 2 3

# out : 1

# 3

# 0 -5 5

# out : 1