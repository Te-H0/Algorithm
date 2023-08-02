import sys
from collections import deque
f = sys.stdin.readline
n, m = map(int, f().split())
l = [0 for i in range(100000+1)]


def sol():
    if n==m:
        return
    dq = deque()
    dq.append(n)
    while l[m] == 0:
        x = dq.popleft()

        if x+1 < 100000+1 and l[x+1] == 0:
            l[x+1] = l[x]+1
            dq.append(x+1)
        if x-1 >= 0 and l[x-1] == 0:
            l[x-1] = l[x]+1
            dq.append(x-1)
        if 2*x < 100000+1 and l[2*x] == 0:
            l[2*x] = l[x]+1
            dq.append(2*x)
    


sol()

print(l[m])
