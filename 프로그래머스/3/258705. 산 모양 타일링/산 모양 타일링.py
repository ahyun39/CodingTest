def solution(n, tops):
    MOD = 10007
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    a[0], b[0] = 0, 1
    
    for k in range(1, n + 1):
        # 이전 삼각형 위에 삼각형이 붙는 경우
        if tops[k - 1] == 1:
            a[k] = (a[k-1] + b[k-1]) % MOD # 3번 방법
            # 1,4번 방법 / 1,2,4번 방법
            b[k] = (2 * a[k-1] + 3 * b[k-1]) % MOD
        # 이전 삼각형 위에 삼각형이 붙지 않는 경우
        else:
            a[k] = (a[k-1] + b[k-1]) % MOD # 4번 방법
            # 2, 4번 방법
            b[k] = (a[k-1] + 2 * b[k-1]) % MOD
            
    return (a[n] + b[n]) % MOD