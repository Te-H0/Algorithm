def solution(prices):
    answer = [0] * len(prices)
    stack = [(prices[0], 1)]  # 가격, 들어온 time(idx + 1) 저장
    # prices[0] 은 1초에 들어온 값 -> prices[idx]는 idx + 1초에 들어온 값

    for i in range(1, len(prices)):  # i + 1 해줘야 현재 시간
        x = prices[i]

        while (
            stack and stack[-1][0] > x
        ):  # stack이 비어있지 않고, 최근 값이 들어올 값보다 작으면
            p, time = stack.pop()  # 값 내려간거니까 pop
            answer[time - 1] = (i + 1) - time  # 현재 시간 - 들어온 시간 = 버틴 시간

        stack.append((x, i + 1))

    while stack:  # 끝까지 안내려간 값들 있으면 처리
        p, time = stack.pop()
        answer[time - 1] = len(prices) - time  # 전체 초(len(prices)) - 들어온 시간
    return answer
