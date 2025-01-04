from itertools import product
def solution(N, number):
    answer = 1
    if N==number:
        return 1
    
    # 8보다 크면 -1
    dp = [set() for _ in range(9)]
    dp[answer].add(N)
    
    for i in range(2,9):
        answer += 1
        dp[answer].add(int(str(N)*i))
        
        for j in range(1,i): 
            for x, y in product(dp[j],dp[i-j]):
                dp[i].update({x+y},{x-y},{x*y})
                if y >0:
                    dp[i].add(x//y)
        if number in dp[i]:
            return answer
        
    return -1