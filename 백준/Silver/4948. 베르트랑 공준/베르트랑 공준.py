import math

def dec(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

while True:
    num = int(input())
    if num == 0: break
    cnt = 0
    for k in range(num+1,(2*num)+1):
        if dec(k): cnt += 1
    print(cnt)