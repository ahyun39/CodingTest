from collections import Counter

def solution(N, stages):
    answer = []
    stage_dict = {i:0 for i in range(1,N+1)}
    stage_cnt = Counter(stages)

    for stage in range(1, max(stages)):
        # stage 이상 도달한 플레이어 수
        stage_dict[stage] = sum(v for k, v in stage_cnt.items() if k >= stage)
    
    failure = []
    for i in range(1, N+1):
        a, b = stage_cnt.get(i, 0), max(stage_dict[i],1)
        failure.append((i, a/b))
    failure.sort(key=lambda x:(-x[1], x[0]))
    for k, v in failure:
        answer.append(k)
    return answer