def solution2(x):
    x_size = len(x)
    mid = x_size // 2
    if x_size == 1:
        if x == "1":
            return 1
        else:
            return 0

    if x[mid] == "0":
        if "1" in x:
            return 0
        else:
            return 1

    result_left = 1
    result_right = 1

    if mid != 1:
        result_left = solution2(x[:mid])
        result_right = solution2(x[mid + 1 :])
    else:
        if x[mid] == "1" or (x[mid] == "0" and "1" not in x):
            return 1
        else:
            return 0

    return result_left * result_right


def solution(numbers):
    answer = []
    for n in numbers:
        x = bin(n)[2:]
        x_size = len(x)

        n = 1
        while True:
            node_count = 2**n - 1
            if x_size <= node_count:
                x = "0" * (node_count - x_size) + x
                break
            n += 1

        answer.append(solution2(x))

    return answer


# [0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
# [0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,0,1,0,0,1]과 다릅니다.
