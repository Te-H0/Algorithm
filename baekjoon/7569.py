import sys
from collections import deque
move = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
m, n, h = map(int, sys.stdin.readline().split())

box = []
zero_tomato_count = 0
one_tomato_idx = []
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 0:
                zero_tomato_count += 1
            elif tmp[j][k] == 1:
                one_tomato_idx.append((i, j, k))
    box.append(tmp)

# 1 익은 토마토, 0 안익은 토마토, -1 아무것도 없음


def bfs():
    global zero_tomato_count
    dq = deque()
    answer = 0
    day = 0
    for i, j, k in one_tomato_idx:
        dq.append((i, j, k, 0))

    while dq:
        x, y, z, day = dq.popleft()
        for m_x, m_y, m_z in move:
            n_x = x + m_x
            n_y = y + m_y
            n_z = z + m_z

            if n_x in range(h) and n_y in range(n) and n_z in range(m) and box[n_x][n_y][n_z] == 0:
                box[n_x][n_y][n_z] = 1
                zero_tomato_count -= 1
                dq.append((n_x, n_y, n_z, day+1))
                answer = day+1
    return answer


if zero_tomato_count == 0:
    print(0)
else:
    answer = bfs()
    if zero_tomato_count != 0:
        print(-1)
    else:
        print(answer)
