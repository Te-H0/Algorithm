import sys
from collections import deque

n = int(sys.stdin.readline())
status = list(map(int, sys.stdin.readline().rstrip()))
goal = list(map(int, sys.stdin.readline().rstrip()))
count = []


def sol(s):
    c_s = s[:]
    press = 0
    for i in range(1, n-1):
        if c_s[i-1] != goal[i-1]:
            c_s[i-1] = 1 - c_s[i-1]
            c_s[i] = 1 - c_s[i]
            c_s[i+1] = 1 - c_s[i+1]
            press += 1

    if c_s[n-2] != goal[n-2]:
        c_s[n-2] = 1 - c_s[n-2]
        c_s[n-1] = 1 - c_s[n-1]
        press += 1
    if c_s == goal:
        return press
    else:
        return int(1e9)


count.append(sol(status))
status[0] = 1-status[0]
status[1] = 1-status[1]
count.append(sol(status)+1)

answer = min(count)

if answer >= int(1e9):
    print(-1)
else:
    print(answer)
