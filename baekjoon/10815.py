# a = list(map(int,input().split())) 띄어쓰기로 구분해서 리스트에 저장
# a,b,c =map(int,input().split()) a,b,c에 각각 저장
# a = sys.stdin.readline().rstrip() 빠른 입력
# print(f"정답은 {answer}입니다.")
# sum(),min(),max(),eval()=>문자형으로 들어온 수학공식 계산,sorted() 리스트 원소가 튜플 같은거면 sorted(a,key=lamda x: x[1])두번째 기준으로 정렬한다는 뜻
import sys

n = int(sys.stdin.readline().rstrip())
l = list(map(int, input().split()))
m = int(sys.stdin.readline().rstrip())
l1 = list(map(int, input().split()))

dic = dict()
for i in l:
    dic[i] = 0

for i in l1:
    if i in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')
