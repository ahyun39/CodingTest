# 1967_노드사이의 거리_골드5

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(cur, target, visited):
    if cur == target:
        return 0  # 자기 자신이면 거리 0
    visited[cur] = True
    for nxt, cost in graph[cur]:
        if not visited[nxt]:
            d = dfs(nxt, target, visited)
            if d != -1:  # 경로를 찾은 경우
                return d + cost
    return -1  # 경로 없음

for _ in range(M):
    a, b = map(int, input().split())
    visited = [False] * (N+1)
    print(dfs(a, b, visited))