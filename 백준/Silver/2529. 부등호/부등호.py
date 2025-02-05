from typing import List, Tuple

def is_valid(x: int, y: int, sign: str) -> bool:
    """부등호 조건을 만족하는지 확인"""
    return (sign == '<' and x < y) or (sign == '>' and x > y)

def find_min_max(k: int, inequality: List[str]) -> Tuple[str, str]:
    """부등호 조건을 만족하는 최댓값과 최솟값을 찾는 함수"""
    def dfs(depth: int, num_list: List[int]):
        """백트래킹을 이용한 숫자 조합 탐색"""
        nonlocal min_val, max_val

        if depth == k + 1:
            num_str = ''.join(map(str, num_list))
            min_val = min(min_val, num_str)
            max_val = max(max_val, num_str)
            return

        for i in range(10):
            if not visited[i]:  # 중복 체크
                if depth == 0 or is_valid(num_list[-1], i, inequality[depth - 1]):  
                    visited[i] = True
                    dfs(depth + 1, num_list + [i])
                    visited[i] = False  # 백트래킹

    min_val, max_val = "9999999999", "0000000000"
    visited = [False] * 10
    dfs(0, [])
    return max_val, min_val

def main():
    """입력을 받아서 결과를 출력하는 메인 함수"""
    k = int(input())
    inequality = list(map(str, input().split()))
    max_val, min_val = find_min_max(k, inequality)
    print(max_val)
    print(min_val)

if __name__ == "__main__":
    main()