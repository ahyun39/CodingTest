# 11660_구간 합 구하기 5_실버1

def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 2차원 누적합 배열 초기화 (N+1 x N+1)
    prefix_sum = [[0] * (N+1) for _ in range(N+1)]

    # 누적합 계산
    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix_sum[i][j] = (
                board[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
            )
            
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        result = (
            prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
        )
        print(result)

solution()