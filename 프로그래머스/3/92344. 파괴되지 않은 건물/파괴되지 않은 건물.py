def solution(board, skill):
    n, m = len(board), len(board[0])
    acc = [[0]*(m+1) for _ in range(n+1)]
    
    for type_num, r1, c1, r2, c2, degree in skill:
        if type_num == 1:
            degree = -degree
        acc[r1][c1] += degree
        acc[r1][c2+1] -= degree
        acc[r2+1][c1] -= degree
        acc[r2+1][c2+1] += degree
    
    # 행 기준 누적합
    for i in range(n+1):
        for j in range(1, m+1):
            acc[i][j] += acc[i][j-1]
    
    # 열 기준 누적합
    for j in range(m+1):
        for i in range(1, n+1):
            acc[i][j] += acc[i-1][j]
    
    # 누적 결과를 실제 보드에 반영하고 카운트
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + acc[i][j] > 0:
                cnt += 1
                
    return cnt