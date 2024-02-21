from collections import deque

def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert_notation(q, base) + T[r] if q else T[r]
        
def solution(n, t, m, p):
    answer = ''
    start, turn = 0, 1
    q = deque(convert_notation(start,n))
    for i in range(1,t*m+1):
        if turn > m: turn = 1
        if not q:
            start += 1
            q = deque(convert_notation(start,n))
        if turn == p: answer += q.popleft()
        else: q.popleft()
        turn += 1
    return answer