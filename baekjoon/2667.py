import sys
move=[(-1,0),(0,1),(1,0),(0,-1)]
answer=[]
f = sys.stdin.readline

n = int(f())

l = [list(map(int,f().rstrip())) for i in range(n)]

def dfs(a,b,cnt): 
    cnt+=1
    l[a][b]=0
    for i in range(4):
        if a+move[i][0]>=0 and a+move[i][0]<n and b+move[i][1]>=0 and b+move[i][1]<n and l[a+move[i][0]][b+move[i][1]]:
            cnt = dfs(a+move[i][0],b+move[i][1],cnt)
    
    return cnt

for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            answer.append(dfs(i,j,0))

answer.sort()
print(len(answer))

for i in answer:
    print(i)
