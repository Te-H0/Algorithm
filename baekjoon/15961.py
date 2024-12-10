import sys

# n 접시, d 초밥 종류, k 연속, c 쿠폰 번호
n,d,k,c = map(int,sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]
li += li

sushi = [0] * 3001

s = set(li[0:k])
answer = 0

if c not in s:
    answer = len(s) + 1
else:
    answer = len(s)
    
for l in li[0:k]:
    sushi[l] += 1
    
start = 1
end = start+k

while start != n:
    # print("======")
    sushi[li[start - 1]] -= 1
    if sushi[li[start - 1]] == 0:
        s.remove(li[start - 1])
    
    now = li[start:end]

    # print(start,n)
    s.add(li[end-1])
    sushi[li[end-1]] += 1
    
    s_size = len(s)
    if c not in s:
        s_size += 1
    # print(start,end, now)
    # print(s, s_size)
    answer = max(answer, s_size)
    
    start += 1
    end += 1
    # print("======")
print(answer)