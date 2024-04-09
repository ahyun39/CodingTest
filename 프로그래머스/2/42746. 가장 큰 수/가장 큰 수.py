def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)  # 각 숫자를 3번 반복하여 비교
    return str(int(''.join(numbers)))