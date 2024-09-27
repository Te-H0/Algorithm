def solution(elements):
    s = set()
    size = len(elements)
    extend_ele = elements+elements
    for i in range(size):
        for j in range(size):
            s.add(sum(extend_ele[j:j+i+1]))
    answer = len(s)
    return answer