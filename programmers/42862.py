def solution(n, lost, reserve):
    both = list(set(reserve) & set(lost))
    reserve = list(set(reserve) - set(both))
    lost = list(set(lost) - set(both))
    answer = 0
    for i in range(n):
        if i+1 not in lost:
            answer += 1
        else:
            if i != 0:
                if i in reserve:
                    reserve.remove(i)
                    answer += 1
                    continue
            if i+2 in reserve:
                reserve.remove(i+2)
                answer += 1
    
    return answer