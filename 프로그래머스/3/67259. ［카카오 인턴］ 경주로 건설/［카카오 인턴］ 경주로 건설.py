import heapq

def solution(board):
    n = len(board)
    INF = int(1e9)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

    dist = [[[INF]*4 for _ in range(n)] for _ in range(n)]
    heap = []

    # 시작점: (0,0) → 4방향 가능 (초기비용 0)
    for d in range(4):
        dist[0][0][d] = 0
        heapq.heappush(heap, (0, 0, 0, d))  # cost, x, y, direction

    while heap:
        cost, x, y, d = heapq.heappop(heap)
        if (x, y) == (n-1, n-1):
            return min(dist[n-1][n-1])

        if dist[x][y][d] < cost:
            continue

        for nd, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                new_cost = cost + 100 if d == nd else cost + 600
                if dist[nx][ny][nd] > new_cost:
                    dist[nx][ny][nd] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny, nd))

    return min(dist[n-1][n-1])
