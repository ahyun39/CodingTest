def solution():
    n = int(input())
    requests = list(map(int, input().split()))
    total_budget = int(input())
    
    lo, hi = 0, max(requests)
    max_local_budget = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        allocated = sum(min(mid, req) for req in requests)

        if allocated <= total_budget:
            max_local_budget = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(max_local_budget)

if __name__ == "__main__":
    solution()