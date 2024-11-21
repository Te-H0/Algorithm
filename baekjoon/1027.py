import sys
INF = 1e9
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
incline = [-INF] * n
possible_view = [0] * n
for i in range(n):
    x1 = i + 1
    y1 = li[i]

    for j in range(i + 1, n):
        x2 = j + 1
        y2 = li[j]

        this_inclie = (y2 - y1) / (x2 - x1)
        if incline[i] < this_inclie:
            possible_view[i] += 1
            possible_view[j] += 1
            incline[i] = this_inclie
print(max(possible_view))
             
