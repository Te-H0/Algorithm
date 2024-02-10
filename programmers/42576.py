from collections import defaultdict
def solution(participant, completion):
    di = defaultdict(int)
    for p in participant:
        di[p] += 1
    for c in completion:
        di[c] -=1
    
    for p in participant:
        if di[p]!=0:
            answer = p
            break
    return answer