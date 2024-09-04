def solution(s):
    answer = 0
    x = 'teho' # x 초기화
    cnt1 = 0 # x 카운트
    cnt2 = 0 # x가 아닌 모든 수 카운트
    
    for alp in s: # 첫 번째 읽었으니 [1]부터
        if cnt1 + cnt2 == 0: # 초기화 상태이면(정해진 x가 없으면)
            x = alp
            cnt1 += 1
        else:
            if x == alp:
                cnt1 += 1
            else:
                cnt2 += 1
        
            if cnt1 == cnt2: #문제에서 분리하는 기준인 x와 x가 아닌 글자의 수가 같아지면
                answer += 1
                cnt1=0
                cnt2 =0
    if cnt1 + cnt2 !=0:
        answer += 1
    return answer