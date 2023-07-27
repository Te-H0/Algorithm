import sys 
sys.setrecursionlimit(100000)
f = sys.stdin.readline

t = int(f())
move = [[-1,0],[0,1],[1,0],[0,-1]]

def dfs(l,check,m,n,a,b):
    if a <0 or a >=n or b < 0 or b >=m or check[a][b]  :
        return
    
    check[a][b]=True

    for i in range(4):
        dfs(l,check,m,n,a+move[i][0],b+move[i][1])




for i in range(t):
    m,n,k = map(int,f().split())
    cnt = 0

    l = [[0] * m for _ in range(n)]
    check = [[True] * m for _ in range(n)]
    for i in range(k):
        a,b = map(int,f().split())

        l[b][a] =1
        check[b][a] = False 

    for i in range(n):
        for j in range(m):
            if not check[i][j]:
                dfs(l,check,m,n,i,j)
                cnt+=1
    
    print(cnt)
    