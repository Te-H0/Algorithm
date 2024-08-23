import sys

move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
n, m, k = map(int, sys.stdin.readline().split())
now_feed = [[5] * n for _ in range(n)] # 지금 양분의 양
feed = list(list(map(int, sys.stdin.readline().split())) for _ in range(n)) # 겨울에 주는 양분의 양
age = [[[] for _ in range(n)] for _ in range(n)] # 지금 살아있는 나무의 나이
answer = m
for _ in range(m):
    x, y, a = map(int, sys.stdin.readline().split())
    age[x - 1][y - 1].append(a)

for _ in range(k):
    for i in range(n):
        for j in range(n):
            age[i][j].sort() # 어린 순서로 정렬
            for k in range(len(age[i][j])):
                # 먹이 먹을 수 있으면 먹어 (봄)
                if age[i][j][k] <= now_feed[i][j]: 
                    now_feed[i][j] -= age[i][j][k]
                    age[i][j][k] += 1
                # 먹이 못먹으면 정렬했으니까 뒤에서부터 나무 다 삭제하고(봄), 삭제한 나무 양분추가(여름)까지
                else:
                    while k < len(age[i][j]):
                        now_feed[i][j] += (age[i][j].pop()) // 2
                        # age[i][j].pop()
                        answer -= 1
                    break
    
    for i in range(n):
        for j in range(n):
            for k in range(len(age[i][j])):
                if age[i][j][k] % 5 == 0: # 나이 5의 배수인 나무 번식, 새로 생긴 나무 나이 1(가을)
                    for m_x, m_y in move:
                        n_x = i + m_x
                        n_y = j + m_y
                        
                        if n_x in range(n) and n_y in range(n):
                            age[n_x][n_y].append(1)
                            answer += 1
            now_feed[i][j] += feed[i][j] # 양분 추가 (겨울)
            

print(answer)