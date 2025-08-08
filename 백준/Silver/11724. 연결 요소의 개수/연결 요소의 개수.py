# 11724_연결 요소의 개수_실버2

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [False] * (N+1)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        bfs(graph, i, visited)

print(cnt)