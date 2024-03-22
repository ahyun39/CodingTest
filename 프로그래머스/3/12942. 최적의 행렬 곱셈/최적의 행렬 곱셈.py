import sys
def solution(matrix_sizes):
    p = []
    for i in range(len(matrix_sizes)):
        if i == len(matrix_sizes)-1:
            p += matrix_sizes[i]
        else:
            p.append(matrix_sizes[i][0])
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1,n):
        m[i][i] = 0
    for l in range(2,n):
        for i in range(1,n-l+1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + list(p)[i-1]*list(p)[k]*list(p)[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n-1]
    return answer