def f():
    N = int(input())
    cnt = 0
    madoka_cat = 0
    while True:
        if madoka_cat == N:
            break
        if madoka_cat + 1 > madoka_cat * 2:
            madoka_cat += 1
        else:
            madoka_cat = min(N, madoka_cat * 2)
        cnt += 1
    return cnt

print(f())