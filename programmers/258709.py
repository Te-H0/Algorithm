from itertools import combinations, product
from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(dice):
    dice_number = [i+1 for i in range(len(dice))]
    
    #[(1,2), (1,3),,,,]
    comb_dice_number = list(combinations(dice_number, len(dice) // 2))
    
    # [(1,2), (1,3)] => [[[1의 주사위 값],[2의 주사위 값]], [[1의 주사위 값],[2의 주사위 값]]]
    comb_dice_element = []
    for cdn in comb_dice_number:
        tmp = []
        for c in cdn:
            tmp.append(dice[c-1])
        comb_dice_element.append(tmp)
    
    # [[[1의 주사위 값],[2의 주사위 값]], [[1의 주사위 값],[2의 주사위 값]]] 
    # -> [[1,2 주사위 값 서로 모두 합], [2,3 주사위 값 서로 모두 합]]
    comb_dice_sum = []
    for cde in comb_dice_element:
        comb_dice_sum.append(sorted([sum(i) for i in product(*cde)]))
    
    result = [[0,0] for _ in range(len(comb_dice_number))] # 승, 패
    
    
    for i in range(len(comb_dice_number)//2):
        a_player = comb_dice_sum[i]
        b_player = comb_dice_sum[-(i+1)]
        
        # 이분 탐색 통해서 a의 값이 b의 어느 인덱스에 위치하는지 찾기 
        # -> 3번째 있으면 0부터니까 3번 이긴것
        # -> b의 길이 - bisect_right하면 진것
        for a in a_player:
            a_win = bisect_left(b_player,a)
            a_lose = len(b_player) -bisect_right(b_player,a)
            result[i][0] += a_win
            result[i][1] += a_lose
            result[-(i+1)][0] += a_lose
            result[-(i+1)][1] += a_win
            
        
    idx = 0
    max_win = 0
    for i, re in enumerate(result):
        if re[0] > max_win:
            idx = i
            max_win = re[0]
    
    return list(comb_dice_number[idx])