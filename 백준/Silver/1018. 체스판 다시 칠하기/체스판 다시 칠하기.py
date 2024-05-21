def min_repaints_to_chessboard(board, M, N):
    chess1 = [['W' if (i+j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]
    chess2 = [['B' if (i+j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]

    def count_repaints(x, y, pattern):
        repaints = 0
        for i in range(8):
            for j in range(8):
                if board[x+i][y+j] != pattern[i][j]:
                    repaints += 1
        return repaints

    min_repaints = float('inf')

    for i in range(M-7):
        for j in range(N-7):
            repaints1 = count_repaints(i, j, chess1)
            repaints2 = count_repaints(i, j, chess2)
            min_repaints = min(min_repaints, repaints1, repaints2)

    return min_repaints

M, N = map(int, input().split())
board = [input().strip() for _ in range(M)]

print(min_repaints_to_chessboard(board, M, N))