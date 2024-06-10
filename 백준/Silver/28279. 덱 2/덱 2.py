from collections import deque
n, deq, print_ = int(input()), deque(), []
for _ in range(n):
    o = input().split()
    if o[0] == '1': deq.appendleft(int(o[1]))
    elif o[0] == '2': deq.append(int(o[1]))
    elif o[0] == '3': print_.append(deq.popleft() if deq else -1)
    elif o[0] == '4': print_.append(deq.pop() if deq else -1)
    elif o[0] == '5': print_.append(len(deq))
    elif o[0] == '6': print_.append(0 if deq else 1)
    elif o[0] == '7': print_.append(deq[0] if deq else -1)
    elif o[0] == '8': print_.append(deq[-1] if deq else -1)
print(*print_, sep='\n')