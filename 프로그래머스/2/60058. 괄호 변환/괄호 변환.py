from collections import deque

def is_right(p):
    left = 0
    for i in range(len(p)):
        if p[i] == "(": left += 1
        else:
            left -= 1
            if left < 0: return False
    if left > 0: return False
    return True

def divide(p):
    left = 0
    for i in range(len(p)):
        if p[i] == "(": left += 1
        else:
            left -= 1
        if left == 0:
            break
    return p[:i+1], p[i+1:]

def solution(p):
    if p == '' or is_right(p): return p
    else:
        u, v = divide(p)
        if is_right(u): 
            return u + solution(v)
        else:
            a = '(' + solution(v) + ')'
            for i in range(1,len(u)-1):
                if u[i] == "(": a += ")"
                else: a += "("
            return a
        
        
    