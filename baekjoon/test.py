import sys
from collections import deque
import heapq

heap = []

arr = []

heapq.heappush(heap, 1)
print(len(heap))

heapq.heappop(heap)
print(len(heap))

