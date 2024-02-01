def solution(n):
    ans = 1
    #n -= 1
    while True:
        if n // 2 < 1:
            break
        t = n / 2
        if t.is_integer():
            n = round(n/2)
        else:
            n -= 1
            ans += 1
    return ans