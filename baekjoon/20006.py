# 매칭 가능한 방이 없으면 새로운 방 만든다
# 방장 기준 -10 +10
# 먼저 생성된 방
# 풀방되면 겜시작
# 플레이어수 p, 닉네임 n, 레벨 l, 방 정원 m
import sys
from collections import deque

# Started! Waiting!
p, m = map(int, sys.stdin.readline().split())
room = []  # [진행상태, 방장레벨, 정원, [(레벨,id), ]]
room_count = 0

for _ in range(p):
    l, n = map(str, sys.stdin.readline().split())
    l = int(l)
    
    # True면 새로운 방 만들어야해
    create_room = True

    idx = 0
    while idx < room_count and create_room:
        status = room[idx][0]
        standard_level = room[idx][1]
        member_info = room[idx][3]
        
        # 들어갈 방이 있으면
        if status == "Waiting!" and standard_level - 10 <= l <= standard_level + 10:
            member_info.append((l, n))
            room[idx][2] += 1
            member_count = room[idx][2]

            if member_count == m:
                room[idx][0] = "Started!"
            create_room = False

        idx += 1

    if create_room:
        status = "Started!" if m == 1 else "Waiting!"
        room.append([status, l, 1, [(l, n)]])
        room_count += 1

for r in room:
    print(r[0])
    r[3].sort(key= lambda r : (r[1]))
    for member in r[3]:
        print(*member)
