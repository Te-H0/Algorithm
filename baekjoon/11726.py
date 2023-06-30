import sys

n=int(sys.stdin.readline())

l=[0]*1000
l[1]=1
l[2]=2

if n!=1:
    for i in range(3,n+1):
        l[i]=l[i-2]+l[i-1]
print(l[n])