import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    left = []
    right = []
    par = str(input())
    for i in range(len(par)):
        if par[i] == '(':
            left.append(par[i])
        elif par[i] == ')':
            if left != []:
                left.pop()
            else:
                right.append(par[i])
                break
    if right != [] or left != []:
        print("NO")
    else:
        print("YES")