def dfs(numbers,li, target,idx, answer):
    if len(li) == len(numbers):
        if sum(li) == target:
            return 1
        # print(li)
        return 0
    
    tmp = li[:]
    a = dfs(numbers, tmp + [numbers[idx]], target, idx + 1, answer)
    b = dfs(numbers, tmp + [-numbers[idx]], target, idx +1, answer)
    return a+b
    
def solution(numbers, target):
    if sum(numbers) < target:
        return 0
    answer = dfs(numbers, [], target,0,0)
    
    return answer