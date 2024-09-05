from collections import Counter
def solution(topping):
    answer = 0
    cheolsoo = Counter(topping)
    brother = set()
    
    for t in topping:
        cheolsoo[t] -= 1
        brother.add(t)
        
        if cheolsoo[t] == 0:
            cheolsoo.pop(t)
        if len(cheolsoo) == len(brother):
            answer += 1
    return answer
#     topping_size = len(topping)
#     dp_left = [0] * topping_size # 본인 포함 왼쪽 토핑 종류의 수
#     dp_right = [0] * topping_size # 본인 포함 오른쪽 토핑 종류의 수
#     answer = 0
    
#     s = set()
#     for i in range(topping_size):
#         s.add(topping[i])
#         dp_left[i] += len(s)
    
#     s.clear()
#     for i in range(topping_size -1 , -1, -1):
#         s.add(topping[i])
#         dp_right[i] += len(s)

#     #dp_left[i], dp_right[i+1] => ex) 1~3, 4~6 토핑 종류의 수
#     for i in range(topping_size - 1): 
#         if dp_left[i] == dp_right[i+1]:
#             answer += 1
    
    
#     return answer

