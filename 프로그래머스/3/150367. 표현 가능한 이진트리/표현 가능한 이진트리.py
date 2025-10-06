import math

def solution(numbers):
    answer = []
    def can_form_tree(binary_str):
        # 이진수 문자열을 완전이진트리 길이(2^n-1)에 맞춰 왼쪽에 0을 채워줌
        length = len(binary_str)
        tree_size = 1
        while tree_size - 1 < length:
            tree_size *= 2
        full_len = tree_size - 1
        # 왼쪽 0 패딩
        s = binary_str.zfill(full_len)
    
        # '1'의 누족 합 계산: prefix[i] = s[:i] 안의 '1'의 개수
        prefix = [0] * (full_len + 1)
        for i, ch in enumerate(s):
            prefix[i+1] = prefix[i] + (1 if ch == '1' else 0)
        
        # s[l:r+1]에 '1'이 하나라도 있는지 O(1)로 확인
        def has_one(l, r):
            if l > r:
                return False
            return (prefix[r+1] - prefix[l]) > 0
        
        # 인덱스 구간 [l, r]를 재귀로 검사
        def is_valid(l, r):
            if l > r or l == r:
                return True
            mid = (l+r) // 2
            root = s[mid]
            
            # 규칙: 루트가 '0'이면 그 서브트리에 '1'이 있으면 안된다.
            if root == '0' and (has_one(l, mid-1) or has_one(mid+1, r)):
                return False
        
            return is_valid(l, mid-1) and is_valid(mid+1, r)
        return is_valid(0, full_len-1)
    for number in numbers:
        if can_form_tree(format(number,'b')):
            answer.append(1)
        else:
            answer.append(0)
    return answer