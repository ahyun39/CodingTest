# commit [BOJ] 2346_풍선 터뜨리기 / 실버3 / 10분 / O
from collections import deque
n = int(input())
balloons = deque(list(map(int,input().split())))
# 풍선 인덱스
balloon_idx = deque([i for i in range(1, n+1)])
idx = []

while balloons:
    move = balloons.popleft()
    idx.append(balloon_idx.popleft())
    # 풍선 안 종이의 값이 양수인 경우 시계방향으로 (값-1)만큼 회전
    if move > 0:
        balloons.rotate(-(move-1))
        balloon_idx.rotate(-(move-1))
    # 풍선 안 종이의 값이 음수인 경우 반시계방향으로 (값)만큼 회전
    else:
        balloons.rotate(-move)
        balloon_idx.rotate(-move)
        
print(*idx)