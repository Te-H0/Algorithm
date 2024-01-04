import sys
from collections import deque, defaultdict

di = defaultdict(int)
n = int(sys.stdin.readline())
answer = [0] * n
li = list(map(int, sys.stdin.readline().split()))
li2 = list(set(li))
li2.sort()

for i in range(len(li2)):
    di[li2[i]] = i

for x in li:
    print(di[x],end=' ')

