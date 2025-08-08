R, C = map(int, input().split())
B = [input() for _ in range(R)]

def dfs(x, y, used):
    global ans
    ans = max(ans, len(used))
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<R and 0<=ny<C and B[nx][ny] not in used:
            dfs(nx, ny, used + B[nx][ny])

ans = 0
dfs(0, 0, B[0][0])
print(ans)