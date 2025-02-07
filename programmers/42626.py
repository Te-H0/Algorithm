import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if K == 0:
        return answer
    elif K!=0 and scoville[1] == 0:
        return -1
    
    while len(scoville) >=2 and scoville[0] < K:
        x1 = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville)
        heapq.heappush(scoville, x1 + x2*2)
        answer += 1
        
    if scoville[0] < K:
        answer = -1
    return answer