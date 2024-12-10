# 서비스 가입자 최대
# 판매액 최대
# 할인율 10, 20, 30, 40

# 자신의 기준 이상 할인하는 이모티콘 모두 구매
# 구매 비용 합이 ~ 이상이면 모두 취소하고 플러스 가입
# user_info = [True, 가격] -> True면 가입, False면 가격 총합 생각
# result = [가입자 수, 현재 금액]
from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    users_count = len(users)
    emoticons_count = len(emoticons)
    discount_ratio = [10, 20, 30, 40]
    discount_products = product(discount_ratio, repeat=emoticons_count)

    for discount in discount_products:
        tmp_answer = [0, 0]

        for limit_discount, limit_total in users:
            # 유저당 총 구매 금액
            user_total_price = 0

            for idx, e in enumerate(emoticons):
                if discount[idx] >= limit_discount:
                    price = e * ((100 - discount[idx]) / 100)
                    user_total_price += price

                    if limit_total <= user_total_price:
                        user_total_price = 0
                        tmp_answer[0] += 1
                        break
            tmp_answer[1] += user_total_price

        if tmp_answer[0] > answer[0]:
            answer = tmp_answer[:]
        elif tmp_answer[0] == answer[0]:
            if tmp_answer[1] > answer[1]:
                answer = tmp_answer[:]

    return answer
