answer = 0
def solution(wallet, bill):
    global answer
    if min(bill) <= min(wallet) and max(bill) <= max(wallet):
        return answer
    if bill[0] > bill[1]:
        bill[0] //= 2
        answer += 1
        solution(wallet, bill)
    elif bill[0] <= bill[1]:
        bill[1] //= 2
        answer += 1
        solution(wallet, bill)
    return answer