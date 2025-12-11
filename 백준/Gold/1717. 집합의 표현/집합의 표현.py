#1717_집합의 표현

n, m = map(int, input().split())

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            self.parent[root_i] = root_j

uf = UnionFind(n+1)

for _ in range(m):
    ord, a, b = map(int, input().split())
    if ord == 0:
        uf.union(a, b)
    else:
        if a == b:
            print("YES")
        elif uf.find(a) == uf.find(b):
            print("YES")
        else:
            print("NO")