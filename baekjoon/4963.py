import sys
from collections import deque
sys.setrecursionlimit(10000)

def dfs(max_w, max_h, l, w, h):
    l[h][w] = 0
    move_x = [1, -1, 0, -1, 1, -1, 0, 1]
    move_y = [0, 0, -1, -1, -1, 1, 1, 1]
    for i in range(8):
        if w+move_x[i] < 0 or w+move_x[i] == max_w or h+move_y[i] < 0 or h+move_y[i] == max_h or l[h+move_y[i]][w+move_x[i]] == 0:
            continue
            
        else:
            dfs(max_w, max_h, l, w+move_x[i], h+move_y[i])
            
def bfs(max_w, max_h, l, w, h):
    move_x = [-1, 1, 0, -1, 1, -1, 0, 1]
    move_y = [0, 0, -1, -1, -1, 1, 1, 1]

    deq=deque()
    l[h][w]=0

    deq.append([h,w])
    

    while deq:
        now = deq.popleft()
        for i in range(8):
            if now[1]+move_x[i] < 0 or now[1]+move_x[i] == max_w or now[0]+move_y[i] < 0 or now[0]+move_y[i] == max_h or l[now[0]+move_y[i]][now[1]+move_x[i]] == 0:
                continue
            
            else:
                l[now[0]+move_y[i]][now[1]+move_x[i]] = 0
                deq.append([now[0]+move_y[i],now[1]+move_x[i]])



while True:
    w, h = map(int, input().split())
    #map(int, read().split())
    if w == 0 and h == 0:
        break
    l = []
    result = 0
    for _ in range(h):
        l.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if l[i][j] == 1:
                result += 1
                bfs(w, h, l, j, i)
                
    print(result)
