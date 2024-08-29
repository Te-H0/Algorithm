from collections import defaultdict

def solution(fees, records):
    first_time, first_fee, per_time, per_fee = fees
    tmp = []
    in_time_di = defaultdict() # 입차 시간
    total_time_di = defaultdict(int) # 총 주차 시간
    default_out_time = 23*60 + 59
    for rec in records:
        time, number, status = rec.split()
        hour, minute = time.split(':')
        
        if status =='IN':
            in_time_di[number] = int(hour) * 60 + int(minute)
        else:
            in_time = in_time_di[number]
            out_time = int(hour) * 60 + int(minute)
            total_time_di[number] += out_time - in_time # 출차한 차 주차시간 저장
            in_time_di.pop(number) # 출차한 차 삭제
        
    
    for number, in_time in in_time_di.items(): # 안나간 차 23:59분으로 출차처리
        total_time_di[number] += default_out_time - in_time
    
    for number, total_time in total_time_di.items():
        total_time -= first_time # 기본 시간 빼기
        tmp_fee = first_fee # 기본 요금 추가
            
        if total_time > 0: # 기본 시간보다 더 주차했으면
            tmp_fee += (total_time // per_time) * per_fee
            if total_time % per_time != 0: # 남은 시간 올림
                tmp_fee += per_fee
                    
        tmp.append((number,tmp_fee))
        
    tmp.sort()
    answer = []
    for t in tmp:
        answer.append(t[1])
    return answer