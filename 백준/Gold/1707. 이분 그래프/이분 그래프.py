from collections import deque

def is_bipartite_graph(V, E, edges):
    # 그래프 초기화
    graph = [[] for _ in range(V + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 색상 배열 (0: 미방문, 1: 색1, -1: 색2)
    colors = [0] * (V+1)

    # BFS를 통한 이분 그래프 판별
    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # 첫 정점을 색1로 칠함

        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if colors[neighbor] == 0:  # 방문하지 않은 경우
                    colors[neighbor] = -colors[current]  # 다른 색으로 칠함
                    queue.append(neighbor)
                elif colors[neighbor] == colors[current]:  # 같은 색이 인접
                    return False
        return True

    # 모든 정점에서 BFS를 수행하여 이분 그래프 여부 확인
    for i in range(1, V + 1):
        if colors[i] == 0:  # 미방문 정점만 확인
            if not bfs(i):
                return False
    return True


def main():
    k = int(input())  # 테스트 케이스 개수
    results = []

    for _ in range(k):
        V, E = map(int, input().split())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))
        # 이분 그래프 여부 판별
        results.append("YES" if is_bipartite_graph(V, E, edges) else "NO")

    print(*results, sep='\n')

if __name__ == "__main__":
    main()