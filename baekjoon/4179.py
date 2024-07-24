import sys
from collections import deque

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
WALL = -2
jihon_start = (0, 0)
r, c = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
# 양수는 불이 생긴 시간, -2는 벽, -1은 지훈이가 다녀간적이 있는 곳
barrier = [[0] * c for _ in range(r)]
first_fire = []


def fire(first_fire): # 벽이 아닌 곳에 불이 퍼지는 시간 기록
    dq = deque()
    for x, y in first_fire:
        if not barrier[x][y]:
            barrier[x][y] = 1
            dq.append((x, y, 1))
    while dq:
        x, y, t = dq.popleft()

        for m_x, m_y in move:
            n_x = x + m_x
            n_y = y + m_y
            if (
                n_x in range(r)
                and n_y in range(c)
                and not barrier[n_x][n_y]
                and barrier[n_x][n_y] != WALL
            ):
                barrier[n_x][n_y] = t + 1
                dq.append((n_x, n_y, t + 1))


def escape(i, j):
    if i == r - 1 or j == c - 1 or i==0 or j==0:
        return 1 # 시작 지점이 탈출 지점인 경우
    dq = deque()
    barrier[i][j] = -1
    dq.append((i, j, 1))
    while dq:
        x, y, t = dq.popleft()
        for m_x, m_y in move:
            n_x = x + m_x
            n_y = y + m_y
            if ( # 다녀간적 없고 -1, 벽 아니고 WALL, 불이 퍼지기 전이면
                n_x in range(r)
                and n_y in range(c)
                and barrier[n_x][n_y] != -1
                and barrier[n_x][n_y] != WALL
                and (barrier[n_x][n_y] > (t + 1) or not barrier[n_x][n_y])
            ):
                if n_x == r - 1 or n_y == c - 1 or n_x ==0 or n_y ==0:
                    return t + 1
                barrier[n_x][n_y] = -1
                dq.append((n_x, n_y, t + 1))
    return "IMPOSSIBLE"


for i in range(r):
    for j in range(c):
        if barrier[i][j] == 0:
            if graph[i][j] == "F":
                first_fire.append((i, j))
            elif graph[i][j] == "#":
                barrier[i][j] = WALL
            elif graph[i][j] == "J":
                jihon_start = (i, j)

fire(first_fire)
print(escape(jihon_start[0], jihon_start[1]))