import heapq

def solution(n, s, a, b, fares):
    INF = int(1e9)
    
    # 그래프 인접 리스트 초기화
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    # 다익스트라 함수
    def dijkstra(start):
        dist = [INF] * (n + 1)
        dist[start] = 0
        heap = [(0, start)]
        
        while heap:
            cost, now = heapq.heappop(heap)
            if dist[now] < cost:
                continue
            for nxt, fare in graph[now]:
                new_cost = cost + fare
                if new_cost < dist[nxt]:
                    dist[nxt] = new_cost
                    heapq.heappush(heap, (new_cost, nxt))
        return dist

    # s, a, b 각각에서의 최단 거리 계산
    dist_s = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)
    
    # 각 지점 k를 합승 분기점으로 가정
    answer = INF
    for k in range(1, n+1):
        total = dist_s[k] + dist_a[k] + dist_b[k]
        answer = min(answer, total)
    
    return answer