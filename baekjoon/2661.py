import sys
from collections import deque
n = int(sys.stdin.readline())

li = []


def sol():

    l = len(li)
    for i in range(1, l//2+1):
        for j in range(l-i*2+1):
            if li[j:j+i] == li[j+i:j+2*i]:
                return False

    if l == n:
        return True

    for i in range(1, 4):
        li.append(i)
        if sol():
            return True
        li.pop()


sol()
for i in li:
    print(i, end='')
