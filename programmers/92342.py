def dfs(idx,cnt,lion,apeach):
    global diff, answer
    if idx == 11 or cnt == 0:
        ap_p, li_p =0,0
        for i in range(11):
            li = lion[i]
            ap = apeach[i]
            
            if li > ap:
                li_p += 10-i
            elif li<ap or (li != 0 and li==ap):
                ap_p += 10-i
        tmp = li_p - ap_p
        
        if diff < tmp:
            diff = tmp
            lion[10] = cnt
            answer = []
            answer.append(lion[:])
        elif diff == tmp:
            lion[10] = cnt
            answer.append(lion[:])
        return
    
    # 이길거야
    if apeach[idx] +1 <= cnt:
        lion[idx] += apeach[idx]+1
        dfs(idx + 1, cnt - (apeach[idx]+1), lion, apeach)
        lion[idx]-= apeach[idx]+1
            
        # 비길거야
    if apeach[idx] <= cnt:
        lion[idx] += apeach[idx]
        dfs(idx + 1, cnt - apeach[idx], lion, apeach)
        lion[idx] -= apeach[idx]
        
    # 질거야
    dfs(idx + 1, cnt, lion, apeach)
    
def solution(n, info):
    global answer
    dfs(0,n,[0]*11,info)
    if answer == []:
        answer.append([-1])
    else:
        answer.sort(reverse = True, key = lambda x : (x[10::-1]))
    return answer[0]

diff = 1
answer = []