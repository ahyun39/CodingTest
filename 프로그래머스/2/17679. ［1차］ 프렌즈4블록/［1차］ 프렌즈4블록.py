def check(i,j,m,n,board):
    directions = [(0, 1), (1, 0), (1, 1)]
    blocks = [[i,j]]
    for dx, dy in directions:
        if board[i][j] == board[i+dx][j+dy] != '0':
            blocks += [[i+dx, j+dy]]
    return blocks if len(blocks) == 4 else []

def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    while True:
        idx = []
        # 블럭 제거하기
        for i in range(m-1):
            for j in range(n-1):
                idx += check(i,j,m,n,board)
        if idx == []: break
        remove_idx = []
        for i in idx:
            if i not in remove_idx: remove_idx.append(i)
        for i in remove_idx: board[i[0]][i[1]] = '0'
        # 블럭 채우기
        for i in range(n):
            for j in range(m-2, -1, -1):
                if board[j][i] != '0':
                    temp, k = board[j][i], j
                    while k < m-1 and board[k+1][i] == '0':
                        k += 1
                    if k != j:
                        board[k][i] = temp
                        board[j][i] = '0'
        answer += len(remove_idx)   
    return answer