import sys
from collections import deque

move = [(0, -1), (0, 1), (-1, 0), (1, 0)]

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
r, c = map(int, sys.stdin.readline().split())


def dfs(r, c, apple, cnt):
    if cnt >= 4:
        return False
    if apple == 2: # 4번 미만의 시도에 사과를 2개 얻었으면 끝
        return True
    

    for m_r, m_c in move:
        n_r = r + m_r
        n_c = c + m_c
        if n_r in range(5) and n_c in range(5) and graph[n_r][n_c] != -1:
            n_apple = apple + graph[n_r][n_c] # 움직일 곳의 사과 여부 추가
            tmp = graph[n_r][n_c] # 재귀 함수 돌아왔을 때 원래 값 복구를 위해 저장
            graph[n_r][n_c] = -1 # 이동한 곳은 장애물로 변경
            if dfs(n_r, n_c, n_apple, cnt + 1): # True면 조건에 맞는 상황 존재하므로 종료
                return 1
            graph[n_r][n_c] = tmp # 재귀에서 돌아오면 안갔던 곳으로 생각하기 위해 복구
    return 0


start_apple = graph[r][c] # 출발하는 지점부터 사과일 수 있으니 출발 지점 값 저장
graph[r][c] = -1 # 출발하는 곳은 어느 경우에나 장애물로 변경된다
print(dfs(r, c, start_apple, 0))
