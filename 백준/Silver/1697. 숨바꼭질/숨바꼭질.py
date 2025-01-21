n, k = map(int,input().split())
def solution(n,k):
    if n >= k : return n-k # 수빈이가 더 멀리 있는 경우에는 x-1 연산만 가능하다.
    elif k == 1 : return 1
    elif k % 2 == 0 : return min(k-n, 1 + solution(n,k//2)) # 동생의 위치가 2로 나눠지는 경우
    else: return 1 + min(solution(n,k+1), solution(n,k-1))
print(solution(n,k))