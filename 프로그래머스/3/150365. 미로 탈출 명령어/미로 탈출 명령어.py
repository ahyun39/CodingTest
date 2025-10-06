import sys
sys.setrecursionlimit(300000000)

def solution(n, m, x, y, r, c, k):
    from collections import deque
    
    # 최소 거리(맨해튼 거리)
    dist = abs(r - x) + abs(c - y)
    if dist > k or (k - dist) % 2 != 0:
        return "impossible"
    
    # 방향 우선순위 (사전순: d < l < r < u)
    directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    
    # BFS 대신 경로 하나만 찾으면 되므로, 그리디 DFS 형태
    def dfs(cx, cy, path, steps):
        if steps == k:
            if (cx, cy) == (r, c):
                return path
            return None
        
        remaining = k - steps
        min_dist = abs(r - cx) + abs(c - cy)
        if min_dist > remaining:  # 남은 걸음으로 도달 불가
            return None
        
        for d, dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 1 <= nx <= n and 1 <= ny <= m:
                new_path = dfs(nx, ny, path + d, steps + 1)
                if new_path:  # 사전순으로 가장 빠른 경로를 찾으면 즉시 반환
                    return new_path
        return None
    
    return dfs(x, y, "", 0) or "impossible"