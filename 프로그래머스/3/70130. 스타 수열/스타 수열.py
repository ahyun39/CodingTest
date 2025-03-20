from collections import Counter

def solution(a):
    if len(a) < 2:
        return 0
    
    count = Counter(a)  # 각 숫자의 빈도수 저장
    answer = 0  # 최대 스타 수열 길이 저장

    for num in count:
        if count[num] <= answer // 2:  # num의 등장 횟수가 이미 최대 길이보다 작다면 건너뜀
            continue
        
        max_ans = 0
        i = 0
        
        while i < len(a) - 1:
            if (a[i] == num and a[i+1] != num) or (a[i] != num and a[i+1] == num):
                max_ans += 2
                i += 1  # 한 쌍을 사용했으므로 다음 칸으로 이동
            i += 1  # 항상 한 칸씩 이동
        
        answer = max(answer, max_ans)

    return answer
