# x, y가 부등호 사인을 만족하는지 확인하는 함수
def is_valid(x, y, sign):
    return (sign == '<' and x < y) or (sign == '>' and x > y)

# 부등호 조건을 만족하는 최댓값과 최솟값을 찾는 함수
def search(k, inequal):

    # 백트래킹을 이용한 숫자 조합 탐색
    def backtrack(depth, num_list): 
        nonlocal min_num, max_num # 전역 변수

        # 숫자 (k+1)개를 모두 선택한 경우 최댓값과 최솟값을 갱신
        if depth == k + 1:
            num_to_str = ''.join(map(str, num_list)) # 리스트를 문자열로 변환
            min_num = min(min_num, num_to_str)
            max_num = max(max_num, num_to_str)
            return

        # 0 ~ 9까지의 숫자를 확인하며 백트래킹 수행
        for i in range(10):
            if not visited[i]:  # 숫자가 사용되지 않았을 경우
                # 첫 번째 숫자가 아니거나, 부등호 조건을 만족하는 경우 진행
                if depth == 0 or is_valid(num_list[-1], i, inequal[depth - 1]):  
                    visited[i] = True # 숫자 사용 표시
                    backtrack(depth + 1, num_list + [i]) # 다음 숫자 선택
                    visited[i] = False  # 백트래킹 (다른 경우의 수 탐색)

    # 최댓값과 최솟값을 저장할 변수
    min_num, max_num = "9999999999", "0000000000" # 문자열 비교를 위해 최대/최소 초기값 설정
    visited = [False] * 10 # 숫자 사용 여부를 저장하는 배열
    backtrack(0, []) # 백트래킹 시작
    return max_num, min_num

def main():
    k = int(input()) # 부등호 개수
    inequal = list(map(str, input().split())) # 부등호 리스트
    max_num, min_num = search(k, inequal)
    print(max_num)
    print(min_num)

if __name__ == "__main__":
    main()