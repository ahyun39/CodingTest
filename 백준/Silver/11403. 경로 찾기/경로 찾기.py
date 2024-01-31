from collections import deque
N = int(input())
in_graph = [list(map(int,input().split())) for _ in range(N)]
out_graph = [[0 for _ in range(N)] for _ in range(N)]
graph = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if in_graph[i][j] == 1: 
            graph[i+1].append(j+1)
            
def bfs(v, connect):
    q = deque()
    q.append(v)
    while q:
        h = q.popleft()
        connect.append(h)
        for i in graph[h]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return connect

for i in range(1,N+1):
    visited = [False]*(N+1)
    connect = []
    connect = bfs(i,connect)
    for j in range(len(connect)):
        if j == 0:
            start = connect[j]
        else:
            out_graph[start-1][connect[j]-1] = 1
            
for g in out_graph:
    print(*g)