# 기록 있는데 수가 다르면, 많이 준사람이 다음 달에 1개 받음
# 기록 없거나 수 같으면, 선물 지수 큰사람이 1개 받음
# 선물 지수 = 준 선물 - 받은 선물
from collections import defaultdict
def solution(friends, gifts):
    di = defaultdict(list) # di[준사람] = [받는사람]
    point = defaultdict(int) 
    total = len(friends)
    result = [0] * total
    for g in gifts:
        a, b = g.split(" ")
        di[a].append(b)
        point[a] += 1
        point[b] -= 1
    for i in range(total):
        for j in range(i+1, total):
            x = friends[i]
            y = friends[j]
            x_count = di[x].count(y) # x -> y
            y_count = di[y].count(x) # y -> x
            
            if x_count == y_count:
                if point[x] > point[y]:
                    result[i]+= 1
                elif point[x] < point[y]:
                    result[j] += 1
            else:
                if x_count > y_count:
                    result[i] += 1
                
                elif x_count < y_count:
                    result[j] += 1
                    

    return max(result)

# muzi -> ryan
# frodo -> muzi
# muzi -> neo
# ryan -> frodo
# ryan -> neo
# frodo -> neo