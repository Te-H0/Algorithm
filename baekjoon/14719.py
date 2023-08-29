from re import A
import sys

h, w = map(int, sys.stdin.readline().split())
block = list(map(int, sys.stdin.readline().split()))
world = [[0]*w for _ in range(h)]
rain = 0

for i in range(w):
    block_height = block[i] - 1
    j = 1
    while block_height >= 0:
        world[h-j][i] = 1
        block_height -= 1
        j += 1


def sol(i, j):
    if j+1 == w:
        return(0, i, j+1)
    if world[i][j+1] == 1:
        return (0, i, j+1)
    count = 1
    move = j+2
    while move < w:
        if world[i][move] == 1:
            break
        count += 1
        move += 1
    if move == w:
        return (0, i, w)
    else:
        return (count, i, move)


i = 0
while i < h:
    j = 0
    while j < w:
        if world[i][j] == 1:
            a, b, c = sol(i, j)
            rain += a
            j = c
        else:
            j += 1
    i += 1

print(rain)
