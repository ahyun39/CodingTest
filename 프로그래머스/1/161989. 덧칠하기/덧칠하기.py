from collections import deque
def solution(n, m, section):
    answer = 0
    section = deque(section)
    while section:
        now = section.popleft()
        answer += 1
        while True:
            if not section: break
            p = section.popleft()
            if p > now + m - 1: 
                section.appendleft(p)
                break
    return answer