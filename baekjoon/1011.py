import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    move = y-x
    answer = 0
    increase = 1
    num = 0
    flag = False

    while num < move:
        num += increase
        answer += 1

        if flag:
            increase += 1
        

        flag = not flag
    print(answer)