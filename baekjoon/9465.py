import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    l = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    
    for i in range(1, n):
        if i > 1:
            l[0][i] = max(l[1][i-1]+l[0][i], l[1][i-2]+l[0][i])
            l[1][i] = max(l[0][i-1]+l[1][i], l[0][i-2]+l[1][i])
        else:
            l[0][i] += l[1][i-1]
            l[1][i] += l[0][i-1]

    print(max(l[0][n-1], l[1][n-1]))
