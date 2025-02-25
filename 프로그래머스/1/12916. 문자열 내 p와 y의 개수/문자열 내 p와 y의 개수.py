def solution(s):
    p_cnt, y_cnt = s.count('p') + s.count('P'), s.count('y') + s.count('Y')
    
    if p_cnt != y_cnt:
        return False
    
    return True