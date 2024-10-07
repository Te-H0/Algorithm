from collections import deque
def solution(s):
    size = len(s)
    dq = deque(s)
    answer = 0
    for _ in range(size):
        tmp = list(dq)[:]
        stack= []
        flag = True
        while dq:
            x = dq.popleft()
            if x in ('[','(','{'):
                stack.append(x)
            elif x == ']' and (not stack or stack[-1] != '['):
                flag = False
                break
            elif x == ')' and (not stack or stack[-1] != '('):
                flag = False
                break
            elif x == '}' and (not stack or stack[-1] != '{'):
                flag = False
                break
            else:
                stack.pop()
                
        if not dq and not stack and flag:
            answer += 1
        
        dq = deque(tmp[1:] + tmp[:1])
    
    return answer