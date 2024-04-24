def push(x):
    q.append(x)

def pop():
    if q:
        ans.append(q.pop(0))
    else:
        ans.append(-1)

def size():
    ans.append(len(q))

def empty():
    if q:
        ans.append(0)
    else:
        ans.append(1)

def front():
    if q:
        ans.append(q[0])
    else:
        ans.append(-1)

def back():
    if q:
        ans.append(q[-1])
    else:
        ans.append(-1)

n = int(input())
q = []
ans = []
for _ in range(n):
    order = str(input())
    if order[:3] == "pus":
        a, b = map(str, order.split())
        push(int(b))
    elif order[:3] == "fro":
        front()
    elif order[:3] == "bac":
        back()
    elif order[:3] == "siz":
        size()
    elif order[:3] == "pop":
        pop()
    else:
        empty()

for a in ans:
    print(a)