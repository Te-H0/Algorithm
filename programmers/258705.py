def solution(n, tops):
    dp1 = [0] * (n+1) # 우 마름모
    dp2 = [0] * (n+1) # 좌 마름모, 세로 마름모, 냅둠
    
    dp2[0] = 1
    
    for i in range(n):
        dp1[i+1] = (dp1[i] + dp2[i]) % 10007
        if tops[i] == 0:
            dp2[i+1] = (dp1[i] + dp2[i] * 2) % 10007
            
        if tops[i] == 1:
            dp2[i+1] = (dp1[i] * 2 + dp2[i] * 3) % 10007
    
    return (dp1[n]+ dp2[n])%10007