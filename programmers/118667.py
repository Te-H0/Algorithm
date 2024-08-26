from collections import deque
def solution2(queue,diff):
    tmp = 0
    idx = -1
    for i in range(len(queue)):
        tmp += queue[i]
        if tmp == diff:
            idx = i+1
            break
        if tmp > diff:
            break
    return idx

def solution(queue1, queue2):
    queue1=deque(queue1)
    queue2=deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    limit_count = len(queue1) + len(queue2)
    total = sum1 + sum2
    if total % 2 != 0:
        return -1
    
    half = total//2
    cnt = 0
    
    while sum1 != half and cnt <limit_count:
        flag = -1
        if sum1 > sum2:
            diff = sum1 - half
            flag = solution2(queue1,diff)
            
        elif sum1 < sum2 :
            diff = sum2 - half
            flag = solution2(queue2,diff)
            
        if flag != -1:
            cnt += flag
            break
        
        else:
            x1 = queue1.popleft()
            x2 = queue2.popleft()
            queue1.append(x2)
            queue2.append(x1)
            sum1 += (x2-x1)
            sum2 += (x1-x2)

            cnt += 2
    if cnt == limit_count:
        cnt = -1
    return cnt