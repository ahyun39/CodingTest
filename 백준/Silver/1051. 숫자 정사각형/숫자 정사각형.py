def f():
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    for s in range(min(N, M), 0, -1):
        for i in range(N - s + 1):
            for j in range(M - s + 1):
                if board[i][j] == board[i+s-1][j] == board[i][j+s-1] == board[i+s-1][j+s-1]:
                    return s * s
    return 1

print(f())