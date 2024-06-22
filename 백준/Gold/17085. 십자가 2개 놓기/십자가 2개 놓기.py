n, m = map(int,input().split())
graph = [str(input()) for _ in range(n)]
def get_max(graph):
    n, m = len(graph), len(graph[0])
    # '#'의 연속된 개수를 저장할 배열
    up = [[0] * m for _ in range(n)]
    down = [[0] * m for _ in range(n)]
    left = [[0] * m for _ in range(n)]
    right = [[0] * m for _ in range(n)]
    # 각 방향에 대해 '#'의 연속된 개수를 구함
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '#':
                up[i][j] = 1 + (up[i-1][j] if i > 0 else 0)
                left[i][j] = 1 + (left[i][j-1] if j > 0 else 0)
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if graph[i][j] == '#':
                down[i][j] = 1 + (down[i+1][j] if i < n-1 else 0)
                right[i][j] = 1 + (right[i][j+1] if j < m-1 else 0)
    # 가능한 모든 십자가 중심 좌표와 크기를 구함
    crosses = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '#':
                max_size = min(up[i][j], down[i][j], left[i][j], right[i][j])
                for size in range(max_size):
                    crosses.append((i, j, size))
    # 두 십자가가 겹치지 않는지 확인하는 함수
    def crosses_overlap_check(c1, c2):
        i1, j1, size1 = c1
        i2, j2, size2 = c2
        # 십자가 1의 범위
        cross1_ = set()
        for k in range(-size1, size1 + 1):
            cross1_.add((i1 + k, j1))
            cross1_.add((i1, j1 + k))
        for k in range(-size2, size2 + 1):
            if (i2 + k, j2) in cross1_ or (i2, j2 + k) in cross1_:
                return False
        return True
    # 최대 넓이의 곱 계산
    max_product = 0
    for i in range(len(crosses)):
        for j in range(i + 1, len(crosses)):
            c1 = crosses[i]
            c2 = crosses[j]
            if crosses_overlap_check(c1, c2):
                area1 = 1 + 4 * c1[2]
                area2 = 1 + 4 * c2[2]
                max_product = max(max_product, area1 * area2)
    return max_product
print(get_max(graph))