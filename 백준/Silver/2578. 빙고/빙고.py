board = []
for _ in range(5):
    board.append(list(map(int,input().split())))

answer = 0
stop = 0

def bingo(board):
    cnt = 0
    cross_left = 0
    cross_right = 0
    for i in range(5):
        w, h = 0, 0
        for j in range(5):
            if board[i][j] == 0:
                w += 1
            if board[j][i] == 0:
                h += 1
        if w == 5:
            cnt += 1
        if h == 5:
            cnt += 1
        if board[i][i] == 0:
            cross_left += 1
        if board[i][4-i] == 0:
            cross_right += 1
    if cross_left == 5:
        cnt += 1
    if cross_right == 5:
        cnt += 1
    return cnt

for _ in range(5):
    mc = list(map(int,input().split()))
    for num in mc:
        answer += 1
        idx = [[b[0],b[1].index(num)] for b in enumerate(board) if num in b[1]]
        board[idx[0][0]][idx[0][1]] = 0
        cnt = bingo(board)
        if cnt >= 3:
            stop = 1
            break
    if stop == 1:
        break
print(answer)