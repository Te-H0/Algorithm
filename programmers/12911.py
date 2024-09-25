def to_binary(n):
    li = []
    while n!= 0:
        li.append(n%2)
        n//= 2
    li.reverse()
    return li

def solution(n):
    one_count = to_binary(n).count(1)
    print(one_count)
    next_number = n+1
    while to_binary(next_number).count(1) != one_count:
        next_number += 1
        
    return next_number