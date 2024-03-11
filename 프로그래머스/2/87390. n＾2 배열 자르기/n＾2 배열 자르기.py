def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row, col = i // n, i % n
        answer.append(max(row, col) + 1)
    return answer