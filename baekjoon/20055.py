import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
durability = deque(l)
check = deque([False]*(2*n))
count = 0
stage = 0

while count < k:
    check.rotate(1)
    durability.rotate(1)

    check[n-1] = False

    for i in range(n-2, -1, -1):
        if check[i] and not check[i+1]:
            if durability[i+1] != 0:
                check[i] == False
                durability[i+1] -= 1
                check[i+1] = True

    check[n-1] = False

    if durability[0] != 0 and not check[0]:
        durability[0] -= 1
        check[0] = True

    stage += 1
    count = durability.count(0)


print(stage)
