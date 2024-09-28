from bisect import bisect_left

def find_number(x, card_packs, pack_count):
    answer = [0, 0]
    if pack_count == 1:
        pack = card_packs[0]
        pack.sort()
        left = 0
        right = len(pack) - 1

        while left < right:
            now_sum = pack[left] + pack[right]

            if now_sum == x:
                answer[0] = pack[left]
                answer[1] = pack[right]
                break
            elif now_sum > x:
                right -= 1
            else:
                left += 1

    else:

        pack1 = card_packs[0]
        pack2 = card_packs[1]
        pack1.sort()
        pack2.sort()

        p1 = 0
        p2 = len(pack2) - 1
        while p1 < len(pack1) and 0 <= p2:
            now_sum = pack1[p1] + pack2[p2]
            # print(pack1[p1], pack2[p2])
            if now_sum == x:
                answer[0] = pack1[p1]
                answer[1] = pack2[p2]
                break

            elif now_sum > x:
                p2 -= 1
            else:
                p1 += 1

        if p1 == len(pack1) or p2 == -1:
            answer = [0, 0]
    return answer


def solution(coin, cards):
    mission = len(cards) + 1
    init_size = len(cards) // 3
    in_my_hand = cards[:init_size]
    cards = cards[init_size:]
    keep = []
    level = 1

    while coin >= 0 and cards:
        
        flag = False
        keep += cards[:2]
        cards = cards[2:]
        keep.sort()

        # 1. 내 손에서 카드 버리기
        tmp = find_number(mission, [in_my_hand], 1)
        if sum(tmp) != 0:  # 버릴 수 있으면
            for t in tmp:
                idx = bisect_left(in_my_hand, t)
                in_my_hand.pop(idx)
            flag = True
            level += 1
            continue

        # 2. coin 1개 쓰고, 내 손 1 + keep 1
        if coin >= 1:

            tmp = find_number(mission, [in_my_hand, keep], 2)
            if sum(tmp) != 0:
                idx1 = bisect_left(in_my_hand, tmp[0])
                idx2 = bisect_left(keep, tmp[1])
                in_my_hand.pop(idx1)
                keep.pop(idx2)
                coin -= 1
                flag = True
                level += 1
                continue

        # 3. coin 2개 쓰고, keep 2개 쓰기
        if coin >= 2:
            tmp = find_number(mission, [keep], 1)
            if sum(tmp) != 0:  # 버릴 수 있으면

                for t in tmp:
                    idx = bisect_left(keep, t)
                    keep.pop(idx)
                coin -= 2
                flag = True
                level += 1
                continue

        break

    return level
