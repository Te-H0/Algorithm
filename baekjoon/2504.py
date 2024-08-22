import sys

open = ["(", "["]
close = [")", "]"]
string = list(sys.stdin.readline().rstrip())
stack = []
# () 2, [] 3
answer = 0
tmp = 1


def multipl_tmp(x):
    global tmp
    if x == "(":
        tmp *= 2
    else:
        tmp *= 3


def valid_bracket(x):
    if (
        not stack
        or (x == ")" and stack[-1] != "(")
        or (x == "]" and stack[-1] != "[")
    ):
        return False

    return True


if string[0] in open:
    stack.append(string[0])
    multipl_tmp(string[0])

    # 시작
    for i in range(1, len(string)):
        x = string[i]
        if x in open:
            stack.append(x)
            multipl_tmp(x)

        else:  # 닫는 괄호 차례
            if not valid_bracket(x):
                answer = 0
                break
            else:
                if x == ")":
                    if string[i - 1] == "(":
                        answer += tmp
                    tmp //= 2
                else:
                    if string[i - 1] == "[":
                        answer += tmp
                    tmp //= 3
                stack.pop()
    if stack:
        answer = 0
print(answer)
