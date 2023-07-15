import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

q= deque()
result = 0
l = [[] for i in range(n)]
check =[False for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    l[a-1].append(b-1)
    l[b-1].append(a-1)

q.append(0)
check[0]= True
while q:
    now =q.popleft()
    for i in l[now]:
        if not check[i]:
            q.append(i)
            check[i] =True
            result +=1

print(result)


         
    



