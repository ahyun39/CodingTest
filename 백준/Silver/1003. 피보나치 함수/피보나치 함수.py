def main():
    T = int(input())
    dp = [(1, 0), (0, 1)] + [(0, 0)] * 40  # 최대 N = 40 (문제 조건)
    
    for i in range(2, 41):
        dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    
    for _ in range(T):
        N = int(input())
        print(dp[N][0], dp[N][1])

if __name__ == "__main__":
    main()