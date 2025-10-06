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
        binary_str = binary_str.zfill(full_len)
    
        # 재귀적으로 유효한 트리인지 검사
        def is_valid(subtree):
            if len(subtree) == 1:
                return True # 리프 노드는 항상 유효
            mid = len(subtree) // 2 # 현재 서브트리의 루트
            root = subtree[mid]
            left = subtree[:mid]
            right = subtree[mid+1:]

            if root == '0' and ('1' in left or '1' in right):
                return False
            return is_valid(left) and is_valid(right)
        return is_valid(binary_str)
    for number in numbers:
        if can_form_tree(format(number,'b')):
            answer.append(1)
        else:
            answer.append(0)
    return answer