from collections import deque
f, s, g, u, d = map(int,input().split())

dist = [0] * (f+1)
q = deque([s])
while q:
    x = q.popleft()
    if x == g:
        print(dist[x])
        break
    for nx in (x+u, x-d):
        if nx == x:
            continue
        if 1 <= nx <= f and not dist[nx]:
            dist[nx] = dist[x] + 1
            q.append(nx)
else:
    print("use the stairs")