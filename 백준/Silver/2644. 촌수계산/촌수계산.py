# 2644_촌수계산_실버2

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())


graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, visited, dist):
    if v == p2:
        return dist
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            res = dfs(next, visited, dist + 1)
            if res != -1:
                return res
    return -1


print(dfs(p1, visited, 0))