from queue import PriorityQueue


# works[0] idx, works[1] 요청시간, Works[2] 소요시간
# disk[0] 소요시간, disk[1] 요청시간, disk[2] idx
# 소요시간, 요청시각, 작업 번호 순
def solution(jobs):
    works = []
    for idx, j in enumerate(jobs):
        works.append((idx, j[0], j[1]))
    works.sort(key=lambda x: x[1])
    answer = 0
    now_time = works[0][1]
    run_time = [0] * len(jobs)
    disk = PriorityQueue()
    while works:
        if works[0][1] == now_time:
            idx, s, l = works.pop(0)
            disk.put((l, s, idx))
        else:
            break
        
    while not disk.empty():
        l, s, idx = disk.get()
        now_time += l
        run_time[idx] = now_time - s
        print("!")
        print(idx, now_time, s)
        print("!")
        print()
            
        while works:
            if works[0][1] <= now_time:
                disk.put((works[0][2], works[0][1], works[0][0]))
                works.pop(0)
            else:
                break
        if disk.empty() and works:
            now_time = works[0][1]
            while works:
                if works[0][1] == now_time:
                    idx, s, l = works.pop(0)
                    disk.put((l, s, idx))
                else:
                    break
        print(run_time)
        print(now_time)
        print(works)

    answer = int(sum(run_time) / len(run_time))
    print(run_time)
    return answer


a = [[0 ,10] ,[0, 9], [0, 17], [2, 9]]

print(solution(a))
