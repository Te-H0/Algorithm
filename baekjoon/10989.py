import sys

n = int(sys.stdin.readline().rstrip())
l=[0]*10000

for i in range(n):
    x= int(sys.stdin.readline().rstrip())
    l[x-1]+=1

for i in range(10000):
    if l[i]!=0:
        while(l[i]!=0):
            print(i+1)
            l[i]-=1