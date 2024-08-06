import sys, math, numpy
answer = []
n,k = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))

def calculator(li,n):
    m = sum(li)/n
    tmp = 0
    for l in li:
        tmp += (l-m)**2
    tmp/=n
    return math.sqrt(tmp)
        
    
    
for i in range(n-k+1):
    for j in range(i+k,n+1):
        l = li[i:j]
        answer.append(calculator(l,j-i))
print(min(answer))
        
        
        