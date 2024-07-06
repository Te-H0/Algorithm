import sys
from collections import defaultdict

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c, n = map(int, sys.stdin.readline().split())

tmp = [list(sys.stdin.readline().strip()) for _ in range(r)]
if n == 1:
    for i in range(r):
        for j in range(c):
            print(tmp[i][j],end='')
        print()
elif n == 2:
    for i in range(r):
        for j in range(c):
            print('O', end='')
        print()
else:
    graph = [[0] * c for _ in range(r)]  # -1 ->  빈칸 , 양수 -> 설치시간
    bomb = defaultdict(list)

    for i in range(r):
        for j in range(c):
            if tmp[i][j] == ".":
                graph[i][j] = 2
                bomb[2].append((i, j))

            elif tmp[i][j] == "O":
                graph[i][j] = 0
                bomb[0].append((i, j))

    for i in range(3, n + 1):
        if i % 2:  # 홀수면 -> 폭발
            tmp2 = list()  # 이번에 폭발하는 위치 저장 후 나중에 한번에 삭제
            if len(bomb[i-3]) != 0: # 이거 안하니까 type Error뜸! None나오는 경우 있어서
                for x, y in bomb.get(i - 3):
                    if graph[x][y] == i-3:  # 여전히 폭탄이 설치되어 있다면
                        tmp2.append((x, y))
                        for m_x, m_y in move:
                            if x + m_x in range(0, r) and y + m_y in range(0, c):
                                tmp2.append((x + m_x, y + m_y))
                for x, y in tmp2:
                    graph[x][y] = -1

        else:  # 짝수면 폭탄설치
            for j in range(r):
                for k in range(c):
                    if graph[j][k] == -1:
                        graph[j][k] = i
                        bomb[i].append((j, k))

    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                print(".", end="")
            else:
                print("O", end="")
        print()


# 0 설치, 2설치, 3 폭발, 4 설치, 5폭발, 6설치,7폭발
