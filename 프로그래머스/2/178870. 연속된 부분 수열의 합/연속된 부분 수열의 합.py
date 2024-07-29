def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    best_range = None

    while right < len(sequence):
        if current_sum == k:
            if best_range is None or (right - left < best_range[1] - best_range[0]) or (right - left == best_range[1] - best_range[0] and left < best_range[0]):
                best_range = (left, right)
                
            current_sum -= sequence[left]
            left += 1
        elif current_sum < k:
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        else:
            current_sum -= sequence[left]
            left += 1

    if best_range:
        return [best_range[0], best_range[1]]
    else:
        return []