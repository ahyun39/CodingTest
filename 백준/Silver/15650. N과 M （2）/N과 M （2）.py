n, m = map(int, input().split())
ans = []
def back():
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1, n+1):
        if (len(ans) == 0 and i not in ans) or (len(ans) > 0 and max(ans) < i):
            ans.append(i)
            back()
            ans.pop()
    return
back()