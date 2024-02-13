N, M, K = map(int, input().split())
graph = [[i + j for j in range(M)] for i in range(1, (N * M) + 1, M)]
ans = 0

if K != 0:
    must_candidates = [(i, j) for i in range(N) for j in range(M) if graph[i][j] == K]
    if must_candidates:
        must = must_candidates[0]
        for i in range(must[0] + 1):
            for j in range(must[1] + 1):
                graph[i][j] = 1 if i == 0 or j == 0 else graph[i-1][j] + graph[i][j-1]
        now = graph[must[0]][must[1]]
        for i in range(must[0], N):
            for j in range(must[1], M):
                graph[i][j] = now if i == must[0] or j == must[1] else graph[i-1][j] + graph[i][j-1]
        ans = graph[-1][-1]
else:
    for i in range(N):
        for j in range(M):
            graph[i][j] = 1 if i == 0 or j == 0 else graph[i-1][j] + graph[i][j-1]
    ans = graph[-1][-1]
print(ans)
