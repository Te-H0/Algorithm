def solution(targets):
    answer = 0
    targets.sort()
    bound = [targets[0][0],targets[0][1]]
    for a,b in targets[1:]:
        if bound[0] <= a < bound[1]:
            bound[0] = max(bound[0],a)
            bound[1] = min(bound[1],b)
        else:
            print(a,b)
            answer += 1
            bound[0] = a
            bound[1] = b
    answer += 1
    return answer
# 1,4 / 3,7    / 4,5 / 4,8     / 5,12 / 10,14 / 11,13
# (3~4)            (4~5)              (11~12)