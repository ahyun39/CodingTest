def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2  # q는 p와 r의 중간 지점
        merge_sort(A, p, q)  # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)  # 병합

def merge(A, p, q, r):
    i = p
    j = q + 1
    t = 0
    tmp = [0] * (r - p + 1)
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            l.append(tmp[t])
            i += 1
        else:
            tmp[t] = A[j]
            l.append(tmp[t])
            j += 1
        t += 1
    while i <= q:
        tmp[t] = A[i]
        l.append(tmp[t])
        i += 1
        t += 1
    while j <= r:
        tmp[t] = A[j]
        l.append(tmp[t])
        j += 1
        t += 1
    for i in range(t):
        A[p + i] = tmp[i]

n, k = map(int,input().split())
arr = list(map(int,input().split()))
l = []

merge_sort(arr, 0, n-1)

if len(l) >= k: print(l[k-1])
else: print(-1)