import sys

x,y = map(int,sys.stdin.readline().split())

gap = y-x
if gap <=1:
    print(gap)
else:
    answer= 1
    i =1
    while True:
        answer+=1
        if i*(i+1) >= gap:
            print(answer)
            break
        answer+=1
        if (i+1)**2 >= gap:
            print(answer)
            break
        i+=1