import sys

s, m = map(int, sys.stdin.readline().split())
li = sys.stdin.readline()
cond = list(map(int, sys.stdin.readline().split()))
now = [0]*4
answer = 0
flag = True
for i in range(m):
    x = li[i]
    if x == "A":
        now[0] += 1
    elif x == "C":
        now[1] += 1
    elif x == "G":
        now[2] += 1
    elif x == "T":
        now[3] += 1


for i in range(4):
    if cond[i] > now[i]:
        flag = False
        break
if flag:
    answer += 1
head = 0
tail = m

while tail < s:
    flag = True

    y = li[head]
    if y == "A":
        now[0] -= 1
    elif y == "C":
        now[1] -= 1
    elif y == "G":
        now[2] -= 1
    elif y == "T":
        now[3] -= 1

    x = li[tail]
    if x == "A":
        now[0] += 1
    elif x == "C":
        now[1] += 1
    elif x == "G":
        now[2] += 1
    elif x == "T":
        now[3] += 1

    for i in range(4):
        if cond[i] > now[i]:
            flag = False
            break
    if flag:
        answer += 1
    head += 1
    tail += 1
print(answer)
