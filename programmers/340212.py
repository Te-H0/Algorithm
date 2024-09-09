def solution2(diffs, times, limit, level):
    times = [0] + times
    puzzle_size = len(diffs)
    count = 0

    for i in range(puzzle_size):
        if diffs[i] > level:
            count += (diffs[i] - level) * (times[i] + times[i + 1]) + times[i + 1]
        else:
            count += times[i + 1]

    return count


def solution(diffs, times, limit):
    answer = 0
    right = max(diffs)
    left = max(1, min(diffs) - 1)

    while left <= right:
        middle = (left + right) // 2

        count = solution2(diffs, times, limit, middle)
        if count <= limit and (answer == 0 or middle < answer):
            answer = middle
            right = middle - 1
        else:
            left = middle + 1

    return answer