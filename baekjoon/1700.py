import sys, heapq

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
multitap = set()
answer = 0

def distance(x):
    hq =[]
    dist = [300] * (k + 1)
    if k-1 <x:
        return
    for i in range(len(li)-1, x , -1):
        dist[li[i]] = i - x 

    for i in range(1, k + 1):
        heapq.heappush(hq, (-dist[i], i))
    return hq

first = 0
for i in range(len(li)):
    if li[i] not in multitap:
        multitap.add(li[i])
        first += 1

    if first == n:
        n=i
        break
    

for i in range(n+1,len(li)):
    hq = distance(i)
    if li[i] not in multitap:
        while True:
            di, e = heapq.heappop(hq)
            if  e in multitap:
                multitap.remove(e)
                multitap.add(li[i])
                answer += 1
                break

print(answer)