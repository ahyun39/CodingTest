# 5567_결혼식_실버2

from collections import deque

n = int(input())
m = int(input())

graph = [[] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([(1, 0)])
invite_friends = 0
visited[1] = True

while q:
    node, cnt = q.popleft()
    visited[node] = True
    if cnt < 2:
        for nnode in graph[node]:
            if not visited[nnode]:
                invite_friends += 1
                visited[nnode] = True
                q.append((nnode, cnt+1))

print(invite_friends)