from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, V, N):
    visited = [False] * (N + 1)
    q = deque([V])
    visited[V] = True
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def f():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(N+1):
        graph[i].sort()
    visited = [False] * (N+1)
    dfs(graph, V, visited)
    print()
    bfs(graph, V, N)

f()