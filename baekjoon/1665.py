import sys, heapq

n = int(sys.stdin.readline())
left_hq = [(100001, -10001)]
right_hq = [10001]
answer = []

def switch():
    while left_hq and right_hq and left_hq[0][1] > right_hq[0]:
            r_x = heapq.heappop(right_hq)
            l_x = heapq.heappop(left_hq)
            heapq.heappush(left_hq, (-r_x, r_x))
            heapq.heappush(right_hq, l_x[1])
            
for i in range(n):
    x = int(sys.stdin.readline())
    if not i % 2:  # 0,2,3,,, left_hq에 넣기
        heapq.heappush(left_hq, (-x, x)) 
    else:
        heapq.heappush(right_hq, x)
        
    switch()
    print(min(left_hq[0][1], right_hq[0]))