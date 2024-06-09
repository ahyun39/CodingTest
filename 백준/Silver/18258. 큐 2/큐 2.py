from collections import deque

n = int(input())
q = deque([])
print_ = []
for _ in range(n):
    o = str(input())
    if len(o) >= 6:
        o, num = map(str,o.split())
    if o == "push":
        q.append(num)
    elif o == "pop":
        if q: print_.append(q.popleft())
        else: print_.append(-1)
    elif o == "size":
        print_.append(len(q))
    elif o == "empty":
        if q: print_.append(0)
        else: print_.append(1)
    elif o == "front":
        if q: print_.append(q[0])
        else: print_.append(-1)
    else:
        if q: print_.append(q[-1])
        else: print_.append(-1)
print(*print_,sep='\n')