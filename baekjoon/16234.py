import sys
from collections import deque
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, l, r = map(int, sys.stdin.readline().rsplit())

answer = 0
li = []

for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))


def bfs(i, j):
    tmp = []
    dq = deque()
    dq.append((i, j))
    tmp.append((i, j))
    check[i][j] = True

    while dq:
        a, b = dq.popleft()

        for i in range(4):
            move_i = a+move[i][0]
            move_j = b+move[i][1]
            if (0 <= move_i < n) and (0 <= move_j < n) and (check[move_i][move_j] == False):
                diff = max(li[a][b]-li[move_i][move_j], -
                           (li[a][b]-li[move_i][move_j]))
                if l <= diff <= r:
                    check[move_i][move_j] = True
                    dq.append((move_i, move_j))
                    tmp.append((move_i, move_j))

    return tmp


while True:
    flag = False
    unites = []
    check = [[False] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] == False:
                unites = bfs(i, j)  # 이게아니라 그냥 unites=해서 처리하고 다음 검사하면될듯

            if len(unites) > 1:
                flag = True
                population = sum(li[x][y] for x, y in unites) // len(unites)
                for x, y in unites:
                    li[x][y] = population

    if flag:
        answer += 1
    else:
        break

print(answer)
