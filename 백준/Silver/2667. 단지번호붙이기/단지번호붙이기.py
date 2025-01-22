def flood_fill(graph, x, y):
    stack = [(x, y)]
    size = 0
    while stack:
        cx, cy = stack.pop()
        if graph[cx][cy] == '1':  # 방문 확인
            graph[cx][cy] = '0'  # 방문 처리
            size += 1
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == '1':
                    stack.append((nx, ny))
    return size

def f():
    global N
    N = int(input())
    graph = [list(input()) for _ in range(N)]  # 문자열을 리스트로 변환
    apartment = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] == '1':
                apartment.append(flood_fill(graph, i, j))

    apartment.sort()
    print(len(apartment))
    print(*apartment, sep='\n')

f()