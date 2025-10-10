def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        unusable_cnt = 0
        can_cross = True
        
        for stone in stones:
            if stone - mid < 0:
                unusable_cnt += 1
            else:
                unusable_cnt = 0
            if unusable_cnt >= k:
                can_cross = False
                break
        if can_cross:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer