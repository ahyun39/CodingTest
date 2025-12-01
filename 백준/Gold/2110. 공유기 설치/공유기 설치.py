# 2110_공유기 설치

N, C = map(int, input().split())
houses = sorted(int(input()) for _ in range(N))

def can_install(mid):
    count = 1
    last = houses[0]

    for i in range(1, N):
        if houses[i] - last >= mid:
            count += 1
            last = houses[i]
        if count >= C:
            return True
    return False

low, high = 1, houses[-1] - houses[0]
answer = 0

while low <= high:
    mid = (low + high) // 2
    if can_install(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)