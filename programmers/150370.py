from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:])
    
    di = defaultdict(int)
    for t in terms:
        di[t[0]] = int(t[2:])
    # print(di)
    for idx, pri in enumerate(privacies):
        type = pri[-1]
        term = di[type]
        # print(term)
        p_year = int(pri[:4])
        p_month = int(pri[5:7]) + term
        p_day = int(pri[8:10]) - 1
        
        if p_month > 12:
            month = p_month
            p_month = month % 12
            p_year += (month  // 12)
            
        if p_day == 0:
            # print('!')
            p_month -= 1
            p_day = 28
        if p_month == 0:
            p_month = 12
            p_year -= 1
        # print(today_year, today_month, today_day)
        # print(p_year, p_month, p_day)
        # print()
        if p_year < today_year or (p_year == today_year and p_month < today_month) or (p_year == today_year and p_month == today_month and p_day < today_day ):
            answer.append(idx+1)
        
    return answer