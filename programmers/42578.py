# a = list(map(int,input().split())) 띄어쓰기로 구분해서 리스트에 저장
# a,b,c =map(int,input().split()) a,b,c에 각각 저장
# a= sys.stdin.readline().rstrip() 빠른 입력
# print(f"정답은 {answer}입니다.")
# sum(),min(),max(),eval()=>문자형으로 들어온 수학공식 계산,sorted() 리스트 원소가 튜플 같은거면 sorted(a,key=lamda x: x[1])두번째 기준으로 정렬한다는 뜻

from itertools import combinations
from math import prod

clothes = [["yellow_hat", "1"], [
    "blue_sunglasses", "1"], ["green_turban", "1"], ["green_turban", "2"], ["green_turban", "2"], ["green_turban", "3"]]


def solution(clothes):
    answer = 0
    answer += len(clothes)
    d = dict()
    l = list()
    l1 = list()
    for i in range(0, len(clothes)):
        if(clothes[i][1] in d):
            d[clothes[i][1]] += 1
        else:
            d[clothes[i][1]] = 1

    for i in d:
        l.append(d[i]+1)
    print(l)
    answer = prod(l)-1

    return answer


print(solution(clothes))
