def solution(phone_book):
    answer = True
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if(len(phone_book[i]) <= len(phone_book[j])):
                if(phone_book[i] == phone_book[j][:len(phone_book[i])]):
                    answer = False
                    break
        if(not answer):
            break
    return answer


phone_book = ["4", "1111", "1111234"]
print(solution(phone_book))
