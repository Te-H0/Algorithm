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
    start_di = defaultdict(list) # start_di[출발노드] = [도착지들]
    end_di = defaultdict(list) # end_di[도착노드] = [출발지들]
    max_node = 0
    
    for edge in edges: # parent리스트 만들기 위함
        for e in edge:
            max_node = max(e, max_node)
    parent = [-1 for i in range(max_node + 1)]

    for start, end in edges:
        start_di[start].append(end)
        end_di[end].append(start)

        # parent는 초기에 -1로 초기화되기 때문에 첫 접근일 때 자신으로 변경해서 존재하는 노드임을 표시
        if parent[start] == -1:
            parent[start] = start
        if parent[end] == -1:
            parent[end] = end

    # 들어오는 간선 없고, 출발하는 간선이 2개이상인 노드는 생성한 노드 (result[0] 값)
    for start, end in start_di.items():
        if len(end_di[start]) == 0 and len(end) >= 2:
            result[0] = start
            break
    start_di.pop(result[0]) # 생성한 노드 제거하면서 관련된 간선 다 제거

    # 그래프 연결하기, 부모가 같으면 같은 그래프
    for start, end in start_di.items():
        for n in end:
            union_parent(parent, start, n)

    # 한번 더 부모 정리하기
    for i in range(1, max_node + 1):
        if i == result[0] or parent[i] == -1:
            continue
        find_parent(parent, i)
    
    # 같은 부모 갖는 노드들을 같은 그래프라고 저장하기 -> graph_di[부모] = [그래프에 포함되는 노드들]
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
            
        if total_node_count == edge_count: # 노드, 간선 수 같으면 도넛 그래프
            doughnut_graph_count += 1
        elif (total_node_count - 1) // 2 == (edge_count - 2) // 2: # 팔자 그래프
            eight_graph_count += 1
        else: # 나머지는 막대 그래프
            straight_graph_count += 1

    result[1] = doughnut_graph_count
    result[2] = straight_graph_count
    result[3] = eight_graph_count
    return result