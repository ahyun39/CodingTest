def solution(gems):
    total_kinds = len(set(gems))
    gem_counter = {}
    answer = [0, len(gems)-1]
    left = 0
    
    for right in range(len(gems)):
        gem = gems[right]
        gem_counter[gem] = gem_counter.get(gem, 0) + 1
        while len(gem_counter) == total_kinds:
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
            left_gem = gems[left]
            gem_counter[left_gem] -= 1
            if gem_counter[left_gem] == 0:
                del gem_counter[left_gem]
            left += 1
    return [answer[0] + 1, answer[1] + 1]