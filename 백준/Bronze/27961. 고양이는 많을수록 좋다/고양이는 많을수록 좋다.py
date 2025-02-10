def f():
    N = int(input())
    cnt, madoka_cat = 0, 0
    while madoka_cat < N:
        madoka_cat = min(N, max(madoka_cat + 1, madoka_cat * 2))
        cnt += 1
    return cnt

print(f())