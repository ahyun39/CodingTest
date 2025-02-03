def check_pattern(board):
    ori_board = {1:'WBWBWBWB', -1:'BWBWBWBW'}
    first = board[0][0]

    replace = 0
    start = 1
    for i in range(8):
        check = ori_board[start]
        for j in range(8):
            if check[j] != board[i][j]:
                replace += 1
        start = -start

    replace2 = 0
    start = -1
    for i in range(8):
        check = ori_board[start]
        for j in range(8):
            if check[j] != board[i][j]:
                replace2 += 1
        start = -start

    return min(replace, replace2)

def f():
    N, M = map(int, input().split())
    board = [str(input()) for _ in range(N)]

    min_ans = float('inf')

    for i in range(N-7):
        for j in range(M-7):
            compare_board = []
            for k in range(8):
                compare_board.append(board[i+k][j:j+8])
            replace = check_pattern(compare_board)
            if min_ans > replace:
                min_ans = replace
    return min_ans

print(f())