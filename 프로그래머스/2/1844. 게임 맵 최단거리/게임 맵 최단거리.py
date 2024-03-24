def solution(maps):
    n, m = len(maps), len(maps[0])
    if maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0: return -1 # 도착점이 막혀있는 경우
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    queue = [(0, 0)] # 시작점 추가
    visited = set([(0, 0)]) # 방문한 위치 저장
    answer = 1

    while queue:
        next_queue = []
        for x, y in queue:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and (nx, ny) not in visited:
                    next_queue.append((nx, ny))
                    visited.add((nx, ny))
        queue = next_queue
        answer += 1
        if (n-1, m-1) in visited: # 도착점에 도달한 경우 반복 중단
            break
        
    else:
        return -1 # 도착점에 도달할 수 없는 경우

    return answer