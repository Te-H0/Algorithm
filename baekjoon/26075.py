import sys

# 0,1
n, m = map(int, sys.stdin.readline().split())

s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())

s_m, t_m = 0, 0
s_one, t_one = list(), list()

for i in range(n + m):
    if s[i] == "1":
        s_one.append(int(i))
    if t[i] == "1":
        t_one.append(i)

for i in range(m):
    s_o = s_one[i]
    t_o = t_one[i]

    dist = 0
    if s_o < t_o:
        dist = t_o - s_o
    else:
        dist = s_o - t_o
    move = dist // 2
    s_m += move
    t_m += move
    if dist % 2 != 0:
        if s_m < t_m:
            s_m += 1
        else:
            t_m += 1
print(s_m**2 + t_m**2)
