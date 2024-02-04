from collections import deque #1tlrks

def bfs(node, graph, max_distance):
    distance = [0] * (N + 1)
    visited = [False] * (N + 1)
    queue = deque([(node, 0)])
    visited[node] = True
    friend = set()
    while queue:
        current, dist = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = dist + 1
                if distance[neighbor] <= max_distance:
                    friend.add(neighbor)
                    queue.append((neighbor, distance[neighbor]))
    return friend

N, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
friend_cnt = [0] * (N + 1)

for _ in range(K):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    friend = bfs(i, graph, 6)
    if friend:
        friend_cnt[i] = len(friend)

friends = set(friend_cnt[1:])
friends = list(friends)

if len(friends) != 1:
    print("Big World!")
else:
    if friends[0] == N - 1:
        print("Small World!")
    else:
        print("Big World!")
