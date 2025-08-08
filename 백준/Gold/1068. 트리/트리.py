N = int(input())
parents = list(map(int, input().split()))
remove_node = int(input())

graph = [[] for _ in range(N)]
root = -1
for i in range(N):
    if parents[i] == -1:
        root = i
    else:
        graph[parents[i]].append(i)

def dfs(node):
    if node == remove_node:
        return 0
    children = [child for child in graph[node] if child != remove_node]
    if not children:
        return 1

    return sum(dfs(child) for child in children)

print(0 if root == remove_node else dfs(root))