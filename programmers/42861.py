def find_parents(x, parents):
    if x != parents[x]:
        parents[x] = find_parents(parents[x], parents)

    return parents[x]


def union(x, y, parents):
    x = find_parents(x, parents)
    y = find_parents(y, parents)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]

    for a, b, c in costs:
        if find_parents(a, parents) != find_parents(b, parents):
            union(a, b, parents)
            answer += c

    return answer
