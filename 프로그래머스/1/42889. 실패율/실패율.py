from collections import Counter

def solution(N, stages):
    stage_cnt = Counter(stages)
    total_players = len(stages)
    failure = []

    for stage in range(1, N+1):
        reached = total_players  # 현재 스테이지 이상 도달한 플레이어
        fail = stage_cnt.get(stage, 0) / reached if reached > 0 else 0
        failure.append((stage, fail))
        total_players -= stage_cnt.get(stage, 0)  # 다음 스테이지 이상 도달자 수 업데이트

    # 실패율 내림차순, 스테이지 번호 오름차순 정렬
    failure.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, _ in failure]