def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0

    for i in range(N):
        num = A[i]
        l, r = 0, N - 1

        while l < r:
            if l == i:
                l += 1
                continue
            if r == i:
                r -= 1
                continue

            total = A[l] + A[r]
            if total == num:
                cnt += 1
                break  # 중복 counting 방지
            elif total < num:
                l += 1
            else:
                r -= 1

    print(cnt)

if __name__ == "__main__":
    main()