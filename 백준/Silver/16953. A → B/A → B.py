from collections import deque

a, b = map(int, input().split())
q = deque([(a, 1)])
ans = -1

while q:
    num, cnt = q.popleft()
    if num == b:
        ans = cnt
        break
    for nxt in (num*2, int(str(num)+'1')):
        if nxt <= b:
            q.append((nxt, cnt+1))

print(ans)