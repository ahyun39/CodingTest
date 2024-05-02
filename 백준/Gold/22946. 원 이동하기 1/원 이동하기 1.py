from collections import deque
from itertools import combinations
import math

def dfs(x):
    ax, ay, ar = circle[x]
    for i in range(x+1,n+1):
        if ch[i] == -1:
            bx, by, br = circle[i]
            d = math.sqrt(((ax-bx)**2) + ((ay-by)**2))
            if abs(ar - br) > d:
                graph[x].append(i)
                graph[i].append(x)
                ch[i] = 1
                dfs(i)

def lfs(L,x):
    global res, st
    if L > res:
        res = L
        st = x
    for y in graph[x]:
        if ch[y] == -1:
            ch[y] = 1
            lfs(L+1,y)
            ch[y] = -1

if __name__ == '__main__':
    n = int(input())
    circle = [list(map(int,input().split())) for _ in range(n)]
    circle.sort(key=lambda x:-x[2])
    circle.insert(0,(0,0,float('inf')))
    graph = [[]*(n+1) for _ in range(n+1)]
    ch = [-1] * (n+1)
    
    dfs(0)

    res = -4
    st = -1
    et = -1

    ch = [-1] * (n+1)
    ch[0] = 1
    lfs(0,0)
    ch = [-1] * (n+1)
    ch[st] = 1
    lfs(0,st)
    print(res)