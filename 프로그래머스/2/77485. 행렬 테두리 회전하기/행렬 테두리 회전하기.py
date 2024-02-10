from collections import deque

def solution(rows, columns, queries):
    answer = []
    board = [[i + j for j in range(columns)] for i in range(1, rows * columns, columns)]
    
    for query in queries:
        a, b, c, d = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        rotate_list = [board[a][i] for i in range(b, d+1)] + [board[i][d] for i in range(a+1, c+1)] + [board[c][i] for i in range(d-1, b-1, -1)] + [board[i][b] for i in range(c-1, a, -1)]
        answer.append(min(rotate_list))
        rotate_list = deque(rotate_list)
        rotate_list.rotate(1)
        rotate_list = list(rotate_list)
        
        j = 0
        for i in range(b, d+1):
            board[a][i] = rotate_list[j]
            j += 1
        for i in range(a+1, c+1):
            board[i][d] = rotate_list[j]
            j += 1
        for i in range(d-1, b-1, -1):
            board[c][i] = rotate_list[j]
            j += 1
        for i in range(c-1, a, -1):
            board[i][b] = rotate_list[j]
            j += 1
    
    return answer