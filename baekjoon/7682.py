import sys
answer = []


def check_win(x):
    print("으악")
    s = set()
    center = x[4]
    start = x[0]
    end = x[8]

    if center != '.' and (x[3] == center == x[5] or x[1] == x[7] == center or x[0] == center == x[8] or x[2] == center == x[6]):
        s.add(center)

    if start != '.' and (start == x[1] == x[2] or start == x[3] == x[6]):
        s.add(start)

    if end != '.' and (x[2] == x[5] == end or x[6] == x[7] == end):
        s.add(end)
    return s


while True:
    print(answer)
    map = list(sys.stdin.readline().rstrip())
    if ''.join(m for m in map) == 'end':
        break

    x_count = map.count('X')
    o_count = map.count('O')
    dot_count = map.count('.')

    if x_count < o_count or x_count-o_count > 1:
        answer.append("invalid")
        continue

    if dot_count == 0 and (x_count -o_count != 1):
        answer.append("invalid")
        continue

    winner_group = check_win(map)

    if len(winner_group) == 0:
        if dot_count==0:
            answer.append("valid")
        else:
            answer.append("invalid")
        continue
 
    if len(winner_group) == 2:
        answer.append("invalid")
        continue

    winner = winner_group.pop()

    if winner == 'X':
        if x_count > o_count:
            answer.append("valid")
        else:
            answer.append("invalid")

    elif winner == 'O':
        if x_count == o_count:
            answer.append("valid")
        else:
            answer.append("invalid")

if len(answer)!=0:
    for a in answer:
        print(a)
