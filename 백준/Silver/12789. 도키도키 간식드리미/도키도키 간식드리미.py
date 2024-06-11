from collections import deque

n = int(input())
students = deque(list(map(int,input().split())))

stack = []
i = 1

while True:
    if not stack and not students: break
    else:
        if students:
            if students[0] == i:
                students.popleft()
                i += 1
            else:
                if stack:
                    if stack[-1] == i:
                        stack.pop()
                        i += 1
                    else:
                        stack.append(students.popleft())
                else:
                    stack.append(students.popleft())
        else:
            if stack:
                if stack[-1] == i: 
                    stack.pop()
                    i += 1
                else:
                    break
if stack or students:
    print("Sad")
else:
    print("Nice")