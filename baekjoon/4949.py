import sys

open = ("(", "[", "{")
close = (")", "]", "}")
bracket = ("()", "[]", "{}")
answer = []
while True:
    result = "yes"
    stack = list()
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    for charac in sentence:
        if charac in open:
            stack.append(charac)
        elif charac in close:
            if len(stack) != 0 and stack[-1] + charac in bracket:
                stack.pop()
            else:
                result = "no"
    
    if len(stack) != 0:
        result = "no"
    answer.append(result)

for a in answer:
    print(a)
