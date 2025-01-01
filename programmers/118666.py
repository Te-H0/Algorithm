# RT, CF, JM, AN
def sol2(s):
    if 'R' in s:
        t = 0
        if s[0] =='R':
            q1=0
            q2=1
        else:
            q1=1
            q2=0
    elif 'C' in s:
        t = 1
        if s[0] =='C':
            q1=0
            q2=1
        else:
            q1=1
            q2=0
    elif 'J' in s:
        t = 2
        if s[0] =='J':
            q1=0
            q2=1
        else:
            q1=1
            q2=0
    elif 'A' in s:
        t = 3
        if s[0] =='A':
            q1=0
            q2=1
        else:
            q1=1
            q2=0
    return t,q1,q2

def solution(survey, choices):
    answer = ''
    score = [[0,0] for _ in range(4)]
    type = [('R','T'),('C','F'),('J','M'),('A','N')]
    
    for idx, s in enumerate(survey):
        t,q1,q2 = sol2(s)
        point = 4 - choices[idx]
        
        if point > 0:
            score[t][q1] += point
        elif point < 0:
            score[t][q2] -= point
    
    for idx, s in enumerate(score):
        if s[0]>=s[1]:
            answer += type[idx][0]
        else:
            answer += type[idx][1]
    return answer