import sys
from collections import deque

n = int(sys.stdin.readline())
l = list()
total = 0
team = deque()
answer = sys.maxsize
for i in range(n):
    l.append(list(map(int, input().split())))



def match_team(answer, idx):

    if len(team) == n/2:
        opposite=list()
        tmp_sum = 0

        for i in range(n):
            if i not in team:
                opposite.append(i)

        for i in range(0, (n//2)-1):
            for j in range(i+1, n//2):
                tmp_sum += l[team[i]][team[j]]+l[team[j]][team[i]]


        for i in range(0, (n//2)-1):
            for j in range(i+1, n//2):
                tmp_sum -= l[opposite[i]][opposite[j]]+l[opposite[j]][opposite[i]]
    

        if answer > abs(tmp_sum):
            answer = abs(tmp_sum)

        return answer

    for i in range(idx, n):
        team.append(i)
        answer = match_team(answer, i+1)

        team.pop()

    return answer

answer = match_team(answer, 0)
print(answer)
