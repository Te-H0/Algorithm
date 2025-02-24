import sys
from bisect import bisect_left
n = int(sys.stdin.readline())

for _ in range(n):
    li = list(map(int,sys.stdin.readline().split()))
    cnt = 0
    for i in range(1,len(li)-1):
        for j in range(i+1,len(li)):
            if li[i] > li[j]:
                li[i],li[j] = li[j],li[i]
                cnt += 1
    print(li[0],cnt)