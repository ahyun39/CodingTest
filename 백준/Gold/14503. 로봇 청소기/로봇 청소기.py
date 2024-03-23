n, m = map(int, input().split())
robot = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

# 방향 설정: 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 전환
def change_direction(d):
    return (d - 1) % 4

# 후진
def back(x, y, d):
    return (x - dx[d], y - dy[d])

answer = 0
while True:
    # 현재 위치 청소
    if board[robot[0]][robot[1]] == 0:
        board[robot[0]][robot[1]] = 2
        answer += 1
    
    # 현재 위치에서의 왼쪽 방향부터 탐색
    moved = False
    for _ in range(4):
        robot[2] = change_direction(robot[2]) # 왼쪽으로 방향 회전
        nx, ny = robot[0] + dx[robot[2]], robot[1] + dy[robot[2]]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0: # 청소할 곳이 있으면 이동
            robot[0], robot[1] = nx, ny
            moved = True
            break
    
    # 네 방향 모두 청소가 되어있거나 벽인 경우 후진
    if not moved:
        nx, ny = back(robot[0], robot[1], robot[2])
        if board[nx][ny] == 1: # 후진할 곳이 벽인 경우 종료
            break
        else:
            robot[0], robot[1] = nx, ny

print(answer)