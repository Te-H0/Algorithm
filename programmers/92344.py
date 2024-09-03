# type 1 공격, 2 회복 
# type, r1, c1, r2, c2, degree
def solution(board, skill):
    n = len(board)
    m = len(board[0])
    tmp = [[0]*(m+1) for _ in range(n+1)]
    
    for s in skill:
        type, r1, c1, r2, c2, degree = s
        if type == 1:
            degree *= -1
            
        tmp[r1][c1] += degree
        tmp[r1][c2 + 1] += -degree
        tmp[r2 + 1][c1] += -degree
        tmp[r2+1][c2+1] += degree
    
    for i in range(1,n+1):
        for j in range(0, m+1):
            tmp[i][j] += tmp[i-1][j]
    
    for i in range(0,n+1):
        for j in range(1, m+1):
            tmp[i][j] += tmp[i][j-1]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + tmp[i][j] >0:
                answer += 1
            
    return answer


# # type 1 공격, 2 회복 
# # type, r1, c1, r2, c2, degree
# def solution(board, skill):
    
#     answer = len(board) * len(board[0])
#     for s in skill:
#         type, r1, c1, r2, c2, degree = s
#         if type == 1:
#             degree *= -1
#         for i in range(r1,r2+1):
#             for j in range(c1, c2+1):
#                 tmp = board[i][j]
#                 board[i][j] += degree
#                 if tmp <= 0 and board[i][j] > 0:
#                     answer += 1
#                 elif tmp >0 and board[i][j] <= 0 :
#                     answer -= 1
        
#     return answer