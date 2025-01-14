def binary_search(K, N, lans):
    left, right = 1, max(lans)
    max_length = 0

    while left <= right:
        mid = (left + right) // 2
        cnt = sum(lan//mid for lan in lans)

        if cnt >= N:
            max_length = mid
            left = mid + 1
        else:
            right = mid - 1
    return max_length

def f():
    K, N = map(int, input().split())
    lans = [int(input()) for _ in range(K)]
    print(binary_search(K, N, lans))

f()