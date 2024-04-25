from collections import deque

def push_front(x):
    dq.appendleft(x)

def push_back(x):
    dq.append(x)

def pop_front():
    if dq:
        ans.append(dq.popleft())
    else:
        ans.append(-1)

def pop_back():
    if dq:
        ans.append(dq.pop())
    else:
        ans.append(-1)

def size():
    ans.append(len(dq))

def empty():
    if dq:
        ans.append(0)
    else:
        ans.append(1)

def front():
    if dq:
        ans.append(dq[0])
    else:
        ans.append(-1)

def back():
    if dq:
        ans.append(dq[-1])
    else:
        ans.append(-1)

n = int(input())
ans = []
dq = deque([])

for _ in range(n):
    order = str(input())
    if order[:3] == "pus":
        a, b = map(str,order.split())
        if a == "push_front":
            push_front(int(b))
        else:
            push_back(int(b))
    elif order[:3] == "pop":
        if order == "pop_front": pop_front()
        else: pop_back()
    elif order[:3] == "siz": size()
    elif order[:3] == "emp": empty()
    elif order[:3] == "fro": front()
    else: back()

for a in ans:
    print(a)