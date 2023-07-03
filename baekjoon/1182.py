n, s = map(int, input().split())
l = list(map(int, input().split()))
cnt =0 
arr=[]
def back_tracking(idx):
    global cnt

    
    if sum(arr) == s and len(arr)>0:
        cnt+=1
        
    if idx ==n:
        return

    for i in range(idx,n):
            arr.append(l[i])
            back_tracking(i+1)
            arr.pop()

back_tracking(0)

print(cnt)




