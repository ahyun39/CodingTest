import sys
import math

MAX = -math.inf
MIN = math.inf

def odd(num_str, res):
    global MIN, MAX
    for le in num_str:
        if int(le) % 2 == 1:
            res += 1
    if len(num_str) == 1: # 수가 하나인 경우
        MIN = min(res, MIN)
        MAX = max(res, MAX)
        return;
    if len(num_str) == 2: # 수가 두개인 경우
        odd(str(int(num_str[0]) + int(num_str[1])), res)
    else: # 수가 세개이상인 경우
        for i in range(1, len(num_str) - 1):
            for j in range(i + 1, len(num_str)):
                odd(str(int(num_str[0:i]) + int(num_str[i:j]) + int(num_str[j:])), res)

odd(sys.stdin.readline().rstrip(), 0)
print(MIN, MAX)