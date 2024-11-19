def binary_search(data, target):
    lo, hi = 0, len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            return False
        elif data[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return True

def solution():
    na, nb = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a_not_in_B = []


    A.sort()
    B.sort()
    for a in A:
        if binary_search(B, a):
            a_not_in_B.append(a)
    print(len(a_not_in_B))
    print(*a_not_in_B)

if __name__ == "__main__":
    solution()