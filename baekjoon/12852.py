import sys
n = int(sys.stdin.readline())
l = [[0, []] for _ in range(n+1)]


l[1][0] = 1
l[1][1] = [1]

for i in range(2, n+1):
    l[i][0] = l[i-1][0] + 1
    l[i][1] = l[i-1][1] + [i]

    if i % 3 == 0:
        if l[i][0] > l[i//3][0] + 1:
            l[i][0] = l[i//3][0] + 1
            l[i][1] = l[i//3][1] + [i]

    if i % 2 == 0:
        if l[i][0] > l[i//2][0] + 1:
            l[i][0] = l[i//2][0] + 1
            l[i][1] = l[i//2][1] + [i]


print(l[n][0] - 1)
for answer in reversed(l[n][1]):
    print(answer, end=" ")
