import sys
from collections import deque

# 8 아래, 4 오, 2 위, 1 왼
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
room = []


def possible_move(x):
    tmp = move[:]
    result = move[:]
    wall = (8, 4, 2, 1)
    wall_idx = 0
    move_idx = 0
    while x > 0:
        if x >= wall[wall_idx]:
            result.remove(tmp[move_idx])
            x -= wall[wall_idx]


        wall_idx += 1
        move_idx += 1
    return result

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    visit[i][j] = True
    answer =[(i,j)]
    while dq:
        x, y = dq.popleft()
        direction = possible_move(graph[x][y])

        for m_x, m_y in direction:
            n_x = x + m_x
            n_y = y + m_y
            if n_x in range(n) and n_y in range(m) and not visit[n_x][n_y]:
                dq.append((n_x,n_y))
                visit[n_x][n_y] = True
                answer.append((n_x,n_y))
    return answer
def is_next_room(room1,room2):
    for r1 in room1:
        for r2 in room2:
            for n_x,n_y in move:
                if r1[0]+n_x == r2[0] and r1[1]+n_y == r2[1]:
                    return True
    return False
            
def join_room():
    biggest_size = 0
    total_room = len(room)
    for i in range(total_room):
        for j in range(i+1,total_room):
            if is_next_room(room[i],room[j]):
                biggest_size= max(biggest_size,len(room[i]) + len(room[j]))
    return biggest_size
            
for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            room.append(bfs(i,j))
            
print(len(room))
print(max(len(r) for r in room ))
print(join_room())