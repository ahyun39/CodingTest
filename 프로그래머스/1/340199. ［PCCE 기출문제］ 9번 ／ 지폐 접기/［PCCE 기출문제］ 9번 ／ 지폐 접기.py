def solution(wallet, bill, answer=0):
    if min(bill) <= min(wallet) and max(bill) <= max(wallet):
        return answer
    idx = 0 if bill[0] > bill[1] else 1
    bill[idx] //= 2
    return solution(wallet, bill, answer + 1)