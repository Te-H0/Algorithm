# a = list(map(int,input().split())) 띄어쓰기로 구분해서 리스트에 저장
# a,b,c =map(int,input().split()) a,b,c에 각각 저장
# a= sys.stdin.readline().rstrip() 빠른 입력
# print(f"정답은 {answer}입니다.")
# sum(),min(),max(),eval()=>문자형으로 들어온 수학공식 계산,sorted() 리스트 원소가 튜플 같은거면 sorted(a,key=lamda x: x[1])두번째 기준으로 정렬한다는 뜻

import heapq
from re import T
from heapq import heappush
from heapq import heappop
program = [[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]
# program = [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]


def solution(program):
    answer = [0 for i in range(11)]
    h = []
    program.sort(key=lambda x: (x[1], x[0]))
    time = 0
    idx = 0

    while(idx != len(program) or len(h)!=0):
        if len(h)==0:
            time = program[idx][1]

            while idx != len(program) and program[idx][1] <= time:
                    heapq.heappush(h, program[idx])
                    idx += 1
        
        temp = heappop(h)
        answer[temp[0]] += time-temp[1]
        time += temp[2]

        while idx != len(program) and program[idx][1] <= time:
                    heapq.heappush(h, program[idx])
                    idx += 1

    
    answer[0] = time
    return answer


print(solution(program))
