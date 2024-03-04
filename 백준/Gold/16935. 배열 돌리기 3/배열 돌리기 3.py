def one(board):
    for i in range(n//2):
        temp = board[i]
        board[i] = board[n-1-i]
        board[n-1-i] = temp
    return board
def two(board,n,m):
    for i in range(m//2):
        left = [board[j][i] for j in range(n)]
        right = [board[j][m-1-i] for j in range(n)]
        for j in range(n):
            board[j][i] = right[j]
            board[j][m-1-i] = left[j]
    return board
def three(board,n,m):
    re_board = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            re_board[j][n-1-i] = board[i][j]
    return re_board, m, n
def four(board,n,m):
    re_board = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            re_board[m-1-j][i] = board[i][j]
    return re_board, m, n
def five(board,n,m):
    re_board = []
    g1 = [board[i][:m//2] for i in range(n//2)]
    g2 = [board[i][m//2:] for i in range(n//2)]
    g3 = [board[i][:m//2] for i in range(n//2,n)]
    g4 = [board[i][m//2:] for i in range(n//2,n)]
    for i in range(len(g2)):
        re_board.append(g3[i] + g1[i])
    for i in range(len(g1)):
        re_board.append(g4[i] + g2[i])
    
    return re_board
def six(board,n,m):
    re_board = []
    g1 = [board[i][:m//2] for i in range(n//2)]
    g2 = [board[i][m//2:] for i in range(n//2)]
    g3 = [board[i][:m//2] for i in range(n//2,n)]
    g4 = [board[i][m//2:] for i in range(n//2,n)]
    for i in range(len(g2)):
        re_board.append(g2[i] + g4[i])
    for i in range(len(g1)):
        re_board.append(g1[i] + g3[i])
    return re_board

n, m, r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
todo = list(map(int,input().split()))

for i in todo:
    if i == 1: result = one(board)
    elif i == 2: result = two(board,n,m)
    elif i == 3: result, n, m = three(board,n,m)
    elif i == 4: result, n, m = four(board,n,m)
    elif i == 5: result = five(board,n,m)
    elif i == 6: result = six(board,n,m)
    board = result

for i in board:
    print(*i)