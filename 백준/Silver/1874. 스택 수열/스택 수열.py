from collections import deque

n = int(input())
l, r, no = deque(), deque(range(1, n+1)), 0
ans = []
for _ in range(n):
    num = int(input())
    while r and r[0] <= num:
        l.append(r.popleft())
        ans.append("+")
    if l and l[-1] == num:
        l.pop()
        ans.append("-")
    else:
        no = 1
        print("NO")
        break
if no == 0:
    print(*ans,sep='\n')