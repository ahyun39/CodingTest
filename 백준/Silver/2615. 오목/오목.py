# 2615_오목_실버1

def check(board, i, j, x1, y1, x2, y2):
    cnt = 1
    ax, ay = i, j
    nx, ny = i + x1, j + y1
    while True:
        if 0 > nx or nx >= 19 or 0 > ny or ny >= 19:
            break
        if board[nx][ny] != board[i][j]:
            break
        cnt += 1
        ax, ay = nx, ny
        nx, ny = nx + x1, ny + y1

    nx, ny = i + x2, j + y2
    while True:
        if 0 > nx or nx >= 19 or 0 > ny or ny >= 19:
            break
        if board[nx][ny] != board[i][j]:
            break
        cnt += 1
        nx, ny = nx + x2, ny + y2
    if cnt == 5:
        return True, ax, ay
    else:
        return False, ax, ay
        
def f():
    board = [list(map(int, input().split())) for _ in range(19)]
    dx, dy = [-1, 1, 1, -1, 0, 0, -1, 1], [-1, 1, -1, 1, -1, 1, 0, 0] # \, /, ㅡ, |
    win = 0
    ax, ay = -1, -1
    for i in range(19):
        for j in range(19):
            if board[i][j] in [1, 2]:
                for k in range(0, 8, 2):
                    is_valid, x, y = check(board, i, j, dx[k], dy[k], dx[k+1], dy[k+1])
                    if is_valid:
                        win = board[i][j]
                        ax, ay = x+1, y+1
                        break
                if win != 0:
                    break
        if win != 0:
            break
    if win != 0:
        print(win)
        print(ax, ay)
    else:
        print(win)
    
f()