menu = [5, 6, 7, 11]
order = [1, 2, 3, 3, 2, 1, 1]
k = 10

# menu = [5, 12, 30]
# order = [1, 2, 0, 1]
# k = 10

# menu = [5, 12, 30]
# order = [2, 1, 0, 0, 0, 1, 0]
# k = 10

# menu = [5]
# order = [0, 0, 0, 0, 0]
# k = 5


def solution(menu, order, k):
    time = 0
    answer = 1
    pre_time = 0
    cafe = []
    cafe.append([order.pop(0), 0])
    while len(cafe) != 0:
        time += k
        while len(cafe) != 0:
            #print(f"----------before pop {time}----------")
            #for i in cafe:
                #print(f"{i} ", end="")
            #print()

            if cafe[0][1]+menu[cafe[0][0]] <= time:
                pre_time = cafe[0][1]+menu[cafe[0][0]]
                cafe.pop(0)
                #print(f"outtt{cafe.pop(0)}")
                if(len(cafe) != 0):
                    cafe[0][1] = pre_time

            else:
                break
        #print(f"----------after pop {time}----------")
        #for i in cafe:
            #print(f"{i} ", end="")
        #print()
        if len(order) == 0:
            break

        cafe.append([order.pop(0), 0])
        if len(cafe) == 1:
            cafe[0][1] = time
        answer = max(len(cafe), answer)

    return answer


print(solution(menu, order, k))
