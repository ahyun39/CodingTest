def solution():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    def is_enough(height):
        return sum((tree - height) for tree in trees if tree > height) >= M

    left, right = 0, max(trees)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if is_enough(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(result)

solution()