# 16953_A -> B_실버2

from collections import deque, defaultdict

a, b = map(int, input().split())

visited = defaultdict(int)

q = deque([(a, 1)])
visited[a] = 0
ans = -1

while q:
    num, cnt = q.popleft()
    if num == b:
        ans = cnt
        break
    
    mul_two, add_one = num * 2, int(str(num) + '1')
    if mul_two <= b:
        if visited[mul_two] > cnt:
            visited[mul_two] = cnt
        q.append((mul_two, cnt+1))
    if add_one <= b:
        if visited[add_one] > cnt:
            visited[add_one] = cnt
        q.append((add_one, cnt+1))

print(ans)