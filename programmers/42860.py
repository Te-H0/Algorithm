def solution(name):
    answer = 0
    n = len(name)

    # min_n = ord('A')
    # print(ord('A'),ord('Z'))
    # 26
    # 1 2 3 4 5
    for x in name:
        answer += ord(x) - ord('A') if ord(x) - ord('A') <= 13 else ord('A') + 26 - ord(x)
    if answer != 0:
        tmp = n - 1
        tmp_li = [n-1]
        if 'A' in set(name):
            l = 0
            r = 0
            
            while l < n:
                if name[l] != 'A':
                    l += 1
                else:
                    r = l
                    while r + 1 < n and name[r + 1] =='A':
                        r += 1
                    tmp_li.append(min((((l-1) if (l-1) > 0 else 0) * 2 + (n-1) - r), (n-r - 1) * 2 + (l-1)))
                    l = r + 1
        answer += min(tmp_li)
    return answer



   