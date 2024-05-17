from collections import deque
n = int(input())
q = deque([i for i in range(1,n+1)])
ans = []
while q:
    ans.append(q.popleft())
    if not q: break
    q.append(q.popleft())
print(*ans)