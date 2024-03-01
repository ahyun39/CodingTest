def divisor(number):
    result = []
    for i in range(1, int(number**(1/2))+1):
        if number%i==0:
            result.append(i)
            if i < number//i:
                result.append(number//i)
    return len(result)
def solution(number, limit, power):
    answer = 0
    div = [divisor(i) for i in range(1,number+1)]
    for i in div:
        if i > limit: answer += power
        else: answer += i
    return answer