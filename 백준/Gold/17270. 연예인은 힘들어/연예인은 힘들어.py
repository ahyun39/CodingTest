import heapq

INF = int(1e10)

def main():
    V, M = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    J, S = map(int, input().split())
    J_distance = [INF] * (V+1)
    S_distance = [INF] * (V+1)

    
    def dijkstra(start, distance):
        q = []
        
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    

    # 지헌
    dijkstra(J, J_distance)

    # 성하
    dijkstra(S, S_distance)

    place = -1
    min_distance_sum = INF

    for i in range(1, V+1):
        if i != J and i != S:
            if J_distance[i] + S_distance[i] < min_distance_sum:
                min_distance_sum = J_distance[i] + S_distance[i]
    
    min_j_dist = INF

    for i in range(V, 0, -1):
        jd, sd = J_distance[i], S_distance[i]
        if i!= J and i != S:
            if jd <= sd and jd + sd == min_distance_sum:
                if min_j_dist >= jd:
                    place = i
                    min_j_dist = jd

    print(place)

if __name__ == "__main__":
    main()