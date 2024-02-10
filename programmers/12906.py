def solution(arr):
    answer = []
    pre = -1
    
    for a in arr:
        if pre!=a:
            answer.append(a)
            pre = a
    return answer