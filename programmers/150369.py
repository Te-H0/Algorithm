def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
            
        answer += (max(len(deliveries), len(pickups))) * 2
        
        tmp = cap
        while deliveries and tmp != 0:
            deliver = deliveries.pop()
            if deliver == 0:
                continue
            if deliver < tmp:
                tmp -= deliver
            elif deliver >= tmp:
                if deliver != tmp:
                    deliveries.append(deliver - tmp)
                tmp = 0
        
        tmp = cap
        while pickups and tmp != 0:
            pickup = pickups.pop()
            if pickup == 0:
                continue
            if pickup < tmp:
                tmp -= pickup
            elif pickup >= tmp:
                if pickup != tmp:
                    pickups.append(pickup - tmp)
                tmp = 0
    
    return answer