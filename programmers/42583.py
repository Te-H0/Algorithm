from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(maxlen = bridge_length)
    
    answer = 0
    total_weight = 0
    truck_cnt = 0
    
    while truck_weights:
        
        if truck_cnt == bridge_length:
            x = bridge.popleft()
            total_weight -= x
            truck_cnt -= 1
        
        now = truck_weights[0]
        if weight >= total_weight + now:
            truck_weights.pop(0)
            bridge.append(now)
            total_weight += now
        else:
            bridge.append(0)
        truck_cnt += 1
        answer += 1
        
    answer += bridge_length
    return answer