from collections import Counter

def solution(topping):
    answer = 0
    prefix_counter = Counter()
    suffix_counter = Counter(topping)
    prefix_count = 0
    suffix_count = len(topping)

    for i in range(1, len(topping) - 1):
        prefix_counter[topping[i-1]] += 1
        prefix_count += 1
        suffix_counter[topping[i-1]] -= 1
        suffix_count -= 1
        
        if suffix_counter[topping[i-1]] == 0:
            del suffix_counter[topping[i-1]]

        if len(prefix_counter) == len(suffix_counter):
            answer += 1

    return answer