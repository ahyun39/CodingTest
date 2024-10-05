n, m = map(int, input().split())
ans = []
def back():
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1, n+1):
        if ans:
            if ans[-1] <= i:
                ans.append(i)
                back()
                ans.pop()
        else:
            ans.append(i)
            back()
            ans.pop()
    return
back()