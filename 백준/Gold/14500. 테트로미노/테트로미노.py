# Block 1 : 1 X 4
def block_one_row(board,i,j):
    row_sum = 0
    for row in range(4):
        if j+row >= M: return False
        else: row_sum += board[i][j+row]
    return row_sum

def block_one_col(board,i,j):
    col_sum = 0
    for col in range(4):
        if i+col >= N: return False
        else: col_sum += board[i+col][j]
    return col_sum

# Block 2 : 2 X 2
def block_two(board,i,j):
    nx = [0, 0, 1, 1] # 1, 2, 3, 4
    ny = [0, 1, 0, 1]
    block_sum = 0
    for n in range(4):
        if i + nx[n] < N and j + ny[n] < M:
            block_sum += board[i+nx[n]][j+ny[n]]
        else: return False
    return block_sum

# Block 3 : 3 X 2
def block_three_row(board,i,j):
    block_sum = 0
    for row in range(3):
        if j+row >= M: return False
        else: block_sum += board[i][j+row]
    add_block = 0
    if i-1 >= 0:
        add_block = max(board[i-1][j], board[i-1][j+2])
    if i+1 < N:
        add_block = max(add_block, board[i+1][j], board[i+1][j+2])
    return block_sum + add_block

def block_three_col(board,i,j):
    block_sum = 0
    for col in range(3):
        if i+col >= N: return False
        else: block_sum += board[i+col][j]
    add_block = 0
    if j-1 >= 0:
        add_block = max(board[i][j-1], board[i+2][j-1])
    if j+1 < M:
        add_block = max(add_block, board[i][j+1], board[i+2][j+1])
    return block_sum + add_block

# Block 4 : 3 X 2
def block_four_row(board,i,j):
    block_sum = 0
    for row in range(2):
        if j+row >= M: return False
        else: block_sum += board[i][j+row]
    add_block = 0
    if i-1 >= 0 and j+2 < M:
        add_block = board[i-1][j+1] + board[i-1][j+2]
    if i+1 < N and j+2 < M:
        add_block = max(add_block, board[i+1][j+1] + board[i+1][j+2])
    return block_sum + add_block

def block_four_col(board,i,j):
    block_sum = 0
    for col in range(2):
        if i+col >= N: return False
        else: block_sum += board[i+col][j]
    add_block = 0
    if j-1 >= 0 and i+2 < N:
        add_block = board[i+1][j-1] + board[i+2][j-1]
    if j+1 < M and i+2 < N:
        add_block = max(add_block, board[i+1][j+1] + board[i+2][j+1])
    return block_sum + add_block

# Block 5 : 2 X 3
def block_five_row(board,i,j):
    block_sum = 0
    for row in range(3):
        if j+row >= M: return False
        else: block_sum += board[i][j+row]
    add_block = 0
    if i-1 >= 0:
        add_block = board[i-1][j+1]
    if i+1 < N:
        add_block = max(add_block,board[i+1][j+1])
    return block_sum + add_block

def block_five_col(board,i,j):
    block_sum = 0
    for col in range(3):
        if i+col >= N: return False
        else: block_sum += board[i+col][j]
    add_block = 0
    if j-1 >= 0:
        add_block = board[i+1][j-1]
    if j+1 < M:
        add_block = max(add_block,board[i+1][j+1])
    return block_sum + add_block

N, M = map(int,input().split()) # 세로, 가로
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if block_one_row(board,i,j): ans = max(ans,block_one_row(board,i,j))
        if block_one_col(board,i,j): ans = max(ans,block_one_col(board,i,j))
        if block_two(board,i,j): ans = max(ans,block_two(board,i,j))
        if block_three_row(board,i,j): ans = max(ans,block_three_row(board,i,j))
        if block_three_col(board,i,j): ans = max(ans,block_three_col(board,i,j))
        if block_four_row(board,i,j): ans = max(ans,block_four_row(board,i,j))
        if block_four_col(board,i,j): ans = max(ans,block_four_col(board,i,j))
        if block_five_row(board,i,j): ans = max(ans,block_five_row(board,i,j))
        if block_five_col(board,i,j): ans = max(ans,block_five_col(board,i,j))
print(ans)