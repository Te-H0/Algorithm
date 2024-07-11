import sys

INF = int(1e9)
n = int(sys.stdin.readline())
now = list(map(int, sys.stdin.readline().strip()))
goal = list(map(int, sys.stdin.readline().strip()))

def flip(l):
    cnt = 0
    for i in range(1, n - 1):
        if l[i - 1] != goal[i - 1]:
            l[i - 1] = not l[i - 1]
            l[i] = not l[i]
            l[i + 1] = not l[i + 1]
            cnt += 1
    if l[n - 2] != goal[n - 2]:
        l[n - 2] = not l[n - 2]
        l[n - 1] = not l[n - 1]
        cnt += 1
    if l[n - 1] != goal[n - 1]:
        return INF
    else:
        return cnt


push_first_switch = now[:]
push_first_switch[0] = not push_first_switch[0]
push_first_switch[1] = not push_first_switch[1]

answer = min(flip(push_first_switch)+1,flip(now))

if answer==INF:
    print(-1)
else:
    print(answer)