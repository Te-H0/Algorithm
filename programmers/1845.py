# a = list(map(int,input().split())) 띄어쓰기로 구분해서 리스트에 저장
# a,b,c =map(int,input().split()) a,b,c에 각각 저장
# a= sys.stdin.readline().rstrip() 빠른 입력
# print(f"정답은 {answer}입니다.")
# sum(),min(),max(),eval()=>문자형으로 들어온 수학공식 계산,sorted() 리스트 원소가 튜플 같은거면 sorted(a,key=lamda x: x[1])두번째 기준으로 정렬한다는 뜻
answer = 0
nums = [3, 3, 3, 2, 2, 2]

nums.sort()
pick = len(nums)/2
count = 0
pre = -1
for n in nums:
    if(n != pre):
        count += 1
        pre = n

if(pick > count):
    answer = count
else:
    answer = pick

print(answer)
