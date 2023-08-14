import sys
import heapq

n = int(sys.stdin.readline())
lesson = []

for i in range(n):
    lesson.append(tuple(map(int, sys.stdin.readline().split())))

lesson.sort()

room = []

heapq.heappush(room, lesson[0][1])

for i in range(1, n):
    if lesson[i][0] >= room[0]:
        heapq.heappop(room)

    heapq.heappush(room, lesson[i][1])
print(len(room))
