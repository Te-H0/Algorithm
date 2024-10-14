import sys
import heapq
n = int(sys.stdin.readline())

lesson=[]
for _ in range(n):
    num, start, end = map(int,sys.stdin.readline().split())
    lesson.append((end,start,num))
lesson.sort(key = lambda x : x[1])
room = [lesson[0]]
answer = 1
heapq.heapify(room)

for l in lesson[1:]:
    #가장 빨리 끝나는 수업
    x = room[0]
        
    # 들어갈 강의실 있으면
    if l[1] >= x[0]:
        heapq.heappop(room)
        
    heapq.heappush(room,l)
    
    answer= max(answer,len(room))
                
print(answer)
    




