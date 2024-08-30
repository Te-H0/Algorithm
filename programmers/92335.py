import math
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2,math.floor(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    tmp = []
    while n > k:
        tmp.append(n % k)
        n = n // k
    
    tmp.append(n)
    tmp.reverse()
    
    tmp2 = "".join(str(t) for t in tmp)
    li = tmp2.split("0")
    
    for l in li:
        if l != "" and is_prime_number(int(l)):
            print(l)
            answer += 1
            
    return answer