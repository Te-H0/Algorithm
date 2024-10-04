from collections import defaultdict


def pointer_up(pointer, step, di):
    for _ in range(step):
        pointer = di[pointer][0]
    return pointer


def pointer_down(pointer, step, di):
    for _ in range(step):
        pointer = di[pointer][1]
    return pointer


def delete(pointer, check, di):
    check[pointer] = False
    pre = di[pointer][0]
    next = di[pointer][1]

    if pre != -1:
        di[pre][1] = next
    if next != -1:
        di[next][0] = pre

    if next == -1:
        pointer = pre
    else:
        pointer = next
    return pointer


def redo(n, row, check, di):
    flag = False
    for i in range(row + 1, n):
        if check[i]:
            di[row][1] = i
            di[i][0] = row
            flag = True
            break
    if not flag:
        di[row][1] = -1
    flag = False

    for i in range(row - 1, -1, -1):
        if check[i]:
            di[row][0] = i
            di[i][1] = row
            flag = True
            break
    if not flag:
        di[row][0] = -1


def solution(n, k, cmd):
    di = defaultdict(list)
    answer = "O" * n
    pointer = k
    trash_box = []
    check = [True] * n

    for i in range(n - 1):
        di[i] = [i - 1, i + 1]
    di[n - 1] = [n - 2, -1]

    for c in cmd:

        command = c[0]

        if command == "U":
            pointer = pointer_up(pointer, int(c[2]), di)
        elif command == "D":
            pointer = pointer_down(pointer, int(c[2]), di)
        elif command == "C":
            trash_box.append(pointer)
            answer[pointer] = 'X'
            pointer = delete(pointer, check, di)

        elif command == "Z":
            row = trash_box.pop()
            check[row] = True
            redo(n, row, check, di)
            answer[row] = "X"
        # print(pointer)
        # print(check)
        # print(list(di.items()))
        # print()
    return answer


solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
