# problems -> [알고력, 코딩력, 얻는 알고력, 얻는 코딩력, 푸는 시간]
 
def solution(alp, cop, problems):
    INF = int(1e9)
    problems.sort(key= lambda x :-x[1])
    max_cop = problems[0][1]
    problems.sort(key= lambda x :-x[0])
    max_alp = problems[0][0]
    problems.sort(key=lambda x: (x[0],x[1]))
    
    # 와..... 이걸 어떻게 생각하냐?
    start_alp_gap = min(alp, max_alp)
    start_cop_gap = min(cop, max_cop)
    
    dp = [[INF] * ((max_cop - start_cop_gap) + 1) for _ in range((max_alp - start_alp_gap) + 1)]
    dp[0][0] =0

    for i in range((max_alp - start_alp_gap) + 1):
        for j in range((max_cop - start_cop_gap) + 1):
            if i < (max_alp - start_alp_gap):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            
            if j < (max_cop - start_cop_gap):
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for min_alp, min_cop, get_alp, get_cop, time in problems:
                    if i >= (min_alp - start_alp_gap) and j >= (min_cop - start_cop_gap):
                        new_alp = min((i + get_alp), max_alp - start_alp_gap)
                        new_cop = min((j + get_cop), max_cop - start_cop_gap)
                        
                        dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + time)
            
    return (dp[(max_alp - start_alp_gap)][(max_cop - start_cop_gap)])