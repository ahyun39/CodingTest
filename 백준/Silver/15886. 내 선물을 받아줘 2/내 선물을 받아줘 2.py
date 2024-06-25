n = int(input())
graph = str(input())
print(sum([1 for i in range(n-1) if graph[i:i+2] == 'EW']))