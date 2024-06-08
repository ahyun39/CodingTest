n = int(input())
stack = []
print_ = []
for _ in range(n):
    o = str(input().strip())
    if len(o) == 1:
        order = int(o)
    else:
        order, num = map(int,o.split())
    if order == 1:
        stack.append(num)
    elif order == 2:
        if stack: print_.append(stack.pop())
        else: print_.append(-1)
    elif order == 3:
        print_.append(len(stack))
    elif order == 4:
        if stack: print_.append(0)
        else: print_.append(1)
    else:
        if stack: print_.append(stack[-1])
        else: print_.append(-1)
print(*print_,sep='\n')