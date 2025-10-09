import heapq

def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]
    # 그래프 구성
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    # dist: 각 노드까지의 "최소 intensity" (초기값 INF)
    INF = 10**18
    dist = [INF] * (n+1)
    
    # 다익스트라 초기화: 모든 gate에서 출발 (intensity=0)
    hq = []
    for g in gates:
        dist[g] = 0
        heapq.heappush(hq, (0, g)) # (intensity, node)
    
    # 다익스트라 변형: 비용은 "현재까지의 max edge weight"
    while hq:
        cur_int, node = heapq.heappop(hq)
        if cur_int > dist[node]:
            continue
        # 만약 node가 summit이면, 그 노드에서 더 확장할 필요가 없도록
        # (확장해도 더 큰 intensity만 나오도록 건너뛰어도 가능)
        if node in summits:
            continue
        
        for nei, w in graph[node]:
            next_int = max(cur_int, w)
            if next_int < dist[nei]:
                dist[nei] = next_int
                heapq.heappush(hq, (next_int, nei))
    
    # 가능한 summit들 중 intensity 최소, 같으면 작은 번호 선택
    summits_sorted = sorted(summits)
    best_summit = 0
    best_int = INF
    for s in summits_sorted:
        if dist[s] < best_int:
            best_int = dist[s]
            best_summit = s
            
    return [best_summit, best_int]