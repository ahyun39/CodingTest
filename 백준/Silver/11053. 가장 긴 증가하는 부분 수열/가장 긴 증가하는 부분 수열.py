def lis(l,A):
    dp = [1] * l
    for i in range(1, l):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def main():
    l = int(input())
    A = list(map(int, input().split()))
    print(lis(l,A))

if __name__ == "__main__":
    main()