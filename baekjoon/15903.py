import sys
import heapq

n,m = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
hq=[]
for x in l:
    heapq.heappush(hq,x)

for _ in range(m):
    x= heapq.heappop(hq)
    y= heapq.heappop(hq)
    heapq.heappush(hq,x+y)
    heapq.heappush(hq,x+y)
    
print(sum(hq))
