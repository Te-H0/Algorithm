import sys
from collections import deque
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
mapp = [[0]*n for _ in range(n)]
turn = deque()
snake = deque()
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    mapp[x-1][y-1] = 1

l = int(sys.stdin.readline())
for _ in range(l):
    x, c = map(str, sys.stdin.readline().split())
    turn.append((int(x), c))

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
move_idx = 0  # 0오른쪽 1아래 2왼쪽 3위
head_x, head_y = 0, 0
time = 1
snake.append((head_x, head_y))
while True:
    head_x, head_y = head_x + move[move_idx][0], head_y + move[move_idx][1]
    # print(head_x, head_y, "!", time, "초")

    if head_x not in range(0, n) or head_y not in range(0, n) or (head_x, head_y) in snake:
        print(time)
        break
    snake.appendleft((head_x, head_y))

    if mapp[snake[0][0]][snake[0][1]] == 0:
        snake.pop()
    else :
        mapp[snake[0][0]][snake[0][1]] = 0

    if turn and turn[0][0] == time:
        if turn[0][1] == 'L':
            move_idx -= 1
            if move_idx == -1:
                move_idx = 3
        else:
            move_idx += 1
            if move_idx == 4:
                move_idx = 0
        turn.popleft()
    time += 1
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D
