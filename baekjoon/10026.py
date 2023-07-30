# 132
import sys
from copy import deepcopy
from collections import deque
f = sys.stdin.readline
move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n = int(f())
l = list()
answer = [0, 0]


def bfs(color, x, y, l):
    check[x][y] = 0
    dq = deque()
    dq.append((x, y))
    while dq:
        a, b = dq.popleft()
        
        for i in range(4):
            # print(f'a+move[i][0] => {a+move[i][0]} // b+move[i][1] => {b+move[i][1]}')
            # print(f'l[a+move[i][0]][b+move[i][1]] => {l[a+move[i][0]][b+move[i][1]]}')
            # print(f'check[a+move[i][0]][b+move[i][1]] => {check[a+move[i][0]][b+move[i][1]]}')
            if a+move[i][0] >= 0 and a+move[i][0] < n and b+move[i][1] >= 0 and b+move[i][1] < n and l[a+move[i][0]][b+move[i][1]] == color and check[a+move[i][0]][b+move[i][1]] == 1:
                dq.append((a+move[i][0], b+move[i][1]))
                check[a+move[i][0]][b+move[i][1]] = 0


def bfs2(color, x, y, l):
    check[x][y] = 0
    dq = deque()
    dq.append((x, y))
    while dq:
        a, b = dq.popleft()
        for i in range(4):
            if a+move[i][0] >= 0 and a+move[i][0] < n and b+move[i][1] >= 0 and b+move[i][1] < n and check[a+move[i][0]][b+move[i][1]] == 1:
                if color == "R" or color == "G":
                    if l[a+move[i][0]][b+move[i][1]] == "R" or l[a+move[i][0]][b+move[i][1]] == "G":
                        dq.append((a+move[i][0], b+move[i][1]))
                        check[a+move[i][0]][b+move[i][1]] = 0
                else:
                    if l[a+move[i][0]][b+move[i][1]] == color:
                        dq.append((a+move[i][0], b+move[i][1]))
                        check[a+move[i][0]][b+move[i][1]] = 0


for i in range(n):
    a = f()
    l.append(list(a))

l2 = deepcopy(l)

check = [[1]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if check[i][j] == 1:
            bfs(l[i][j], i, j, l)
            answer[0] += 1

check = [[1]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if check[i][j] == 1:
            bfs2(l[i][j], i, j, l2)
            answer[1] += 1

for i in answer:
    print(i,end=' ')
