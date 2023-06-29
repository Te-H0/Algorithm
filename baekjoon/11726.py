import sys

n=int(sys.stdin.readline())

l=[0]*(n+1)
l[1]=1
l[2]=2
sum = 0
for i in range(3,n+1):
    l[i]=l[i-2]+l[i-1]
print(l[n])