n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))

def bomb(board,i,j):
    bomb_cnt = 0
    if i-1 >= 0:
        if j-1 >= 0:
            if board[i-1][j-1] == '*':
                bomb_cnt += 1
        if board[i-1][j] == '*':
            bomb_cnt += 1
        if j+1 < len(board[0]):
            if board[i-1][j+1] == '*':
                bomb_cnt += 1
    if j-1 >= 0:
        if board[i][j-1] == '*':
            bomb_cnt += 1
    if board[i][j] == '*':
        return '*'
    if j+1 < len(board[0]):
        if board[i][j+1] == '*':
            bomb_cnt += 1
    if i+1 < len(board[0]):
        if j-1 >= 0:
            if board[i+1][j-1] == '*':
                bomb_cnt += 1
        if board[i+1][j] == '*':
            bomb_cnt += 1
        if j+1 < len(board[0]):
            if board[i+1][j+1] == '*':
                bomb_cnt += 1
    return bomb_cnt

open_board = []
for _ in range(n):
    open_board.append(list(input()))

bomb_open = 0
for i in range(n):
    for j in range(n):
        if open_board[i][j] == 'x':
            open_board[i][j] = bomb(board,i,j)
            if open_board[i][j] == '*':
                bomb_open += 1


if bomb_open > 0:
    for t in range(n):
        for k in range(n):
            if board[t][k] == '*':
                open_board[t][k] = '*'
for o in open_board:
    print(*o,sep='')