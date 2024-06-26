INF = int(1e9)

n, m = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

connect_cnt, person = INF, 0
for i in range(1, n+1):
    if sum(graph[i][1:n+1]) < connect_cnt:
        connect_cnt, person = sum(graph[i][1:n+1]), i
print(person)