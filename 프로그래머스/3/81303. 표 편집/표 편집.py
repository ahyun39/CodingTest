def solution(n, k, cmd):
    # 이전/다음 노드를 기록하는 연결 리스트 테이블
    prev = [i-1 for i in range(n)]
    next = [i+1 for i in range(n)]
    next[-1] = -1 # 마지막 행은 다음 없음
    
    # 삭제된 행을 스택으로 관리 (복구 시 꺼내기 위해)
    stack = []
    # 현재 선택된 행
    cur = k
    # 최종 상태 테이블 (0: 존재, X: 삭제)
    result = ["O"]*n
    
    for c in cmd:
        if c[0] == "U": # 위로 이동
            x = int(c.split()[1])
            for _ in range(x):
                cur = prev[cur]
        elif c[0] == "D": # 아래로 이동
            x = int(c.split()[1])
            for _ in range(x):
                cur = next[cur]
        elif c[0] == "C": # 삭제
            stack.append(cur)
            result[cur] = "X"
            
            # 연결 끊기
            if prev[cur] != -1:
                next[prev[cur]] = next[cur]
            if next[cur] != -1:
                prev[next[cur]] = prev[cur]
            
            # 다음 행 선택 (없으면 위 행 선택)
            if next[cur] != -1:
                cur = next[cur]
            else:
                cur = prev[cur]
        else: # 복구
            recover = stack.pop()
            result[recover] = "O"
            if prev[recover] != -1:
                next[prev[recover]] = recover
            if next[recover] != -1:
                prev[next[recover]] = recover
    return ''.join(result)