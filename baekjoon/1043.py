import sys

n, m = map(int, sys.stdin.readline().split())  # n은 사람 수, m은 파티의 수
know_people = set(list(map(int, sys.stdin.readline().split()))[1:])

party_list = []
for i in range(m):
    party_list.append(list(map(int, sys.stdin.readline().split()))[1:]) # 파티 목록 저장

pre_know_size = len(know_people) # 진실을 알고 있는 사람의 수가 바뀌지 않으면 업데이트 끝난 것.

while True:
    for party in party_list:
        for p in party:
            if p in know_people:
                # 해당 파티에 진실을 알고있는 사람이 있다면 그 파티에 있는 사람 모두 합집합 처리
                know_people.update(party) 
                break

    if pre_know_size == len(know_people):
        break
    pre_know_size = len(know_people)

answer = 0
for party in party_list: 
    # 파티와 진실을 알고 있는 리스트의 교집합 -> 이것의 사이즈가 0이면 거짓말해도 되는 파티
    if len(set(party) & know_people) == 0:
        answer += 1
print(answer)


# 4 3
# 0
# 2 1 2
# 1 3
# 3 2 3 4

# 5 4
# 1 5
# 2 1 2
# 2 2 3
# 2 3 4
# 2 4 5

# 10 9
# 4 1 2 3 4
# 2 1 5
# 2 2 6
# 1 7
# 1 8
# 2 7 8
# 1 9
# 1 10
# 2 3 10
# 1 4
# [0, 1, 2, 3, 4, 1, 2, 7, 7, 9, 3]
