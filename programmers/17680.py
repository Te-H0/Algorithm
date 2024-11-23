from collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    check = set()
    answer = 0
    for city in cities:
        city = city.lower()
        if city not in check:
            answer += 5

            if cacheSize != 0 and len(cache) == cacheSize:
                check.remove(cache[-1])

            cache.appendleft(city)
            if len(check) < cacheSize:
                check.add(city)
        else:
            answer += 1

            if len(cache) != 0:
                cache.remove(city)
            cache.appendleft(city)

    return answer
