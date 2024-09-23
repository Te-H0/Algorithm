# 도넛 - n개 정점, n개 간선
# 막대 - n개 정점, n-1 간선
# 8자 - 2n+1 정점, 2n+2 간선 => 같은 크기 도넛 2개에/ 정점 하나 추가해 결합
# answer = 추가한 정점 번호, 도넛 수, 막대 수, 8자 수

# 들어오는 간선 없는 정점 -> 막대 시작 정점 or 추가한 정점 -> 해당 정점에서 출발하는 간선 2개 이상이면 추가한 정점
from collections import defaultdict

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    if parent[a] == -1:
        parent[a] = a
    if parent[b] == -1:
        parent[b] = b
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(edges):
    result = [0, 0, 0, 0]
    start_di = defaultdict(list)
    end_di = defaultdict(list)
    max_node = 0
    for edge in edges:
        for e in edge:
            max_node = max(e, max_node)
    parent = [-1 for i in range(max_node + 1)]

    for start, end in edges:
        start_di[start].append(end)
        end_di[end].append(start)

        if parent[start] == -1:
            parent[start] = start
        if parent[end] == -1:
            parent[end] = end

    for start, end in start_di.items():
        if len(end_di[start]) == 0 and len(end) >= 2:
            result[0] = start
            break
    start_di.pop(result[0])

    for start, end in start_di.items():
        for n in end:
            union_parent(parent, start, n)

    for i in range(1, max_node + 1):
        if i == result[0] or parent[i] == -1:
            continue
        find_parent(parent, i)
    
    graph_di = defaultdict(list)
    for i in range(1, max_node + 1):
        if i == result[0] or parent[i] == -1:
            continue
        graph_di[parent[i]].append(i)

    doughnut_graph_count = 0  # 도넛 - n개 정점, n개 간선
    straight_graph_count = 0  # 막대 순환(x) - n개 정점, n-1 간선
    eight_graph_count = 0  # 8자 - 2n+1 정점, 2n+2 간선

    for child in graph_di.values():
        total_node_count = len(child)
        edge_count = 0
        for c in child:
            edge_count += len(start_di[c])
        # print(f'parent -> {parent_node}, node -> {total_node_count}, edge -> {edge_count}')
        if total_node_count == edge_count:
            doughnut_graph_count += 1
        elif (total_node_count - 1) // 2 == (edge_count - 2) // 2:
            eight_graph_count += 1
        else:
            straight_graph_count += 1

    result[1] = doughnut_graph_count
    result[2] = straight_graph_count
    result[3] = eight_graph_count
    return result