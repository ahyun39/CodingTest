from collections import deque

def solution(rc, operations):
    n, m = len(rc), len(rc[0])
    
    # 행의 양쪽 끝과 가운데를 분리
    left = deque([row[0] for row in rc])          # 왼쪽 열
    right = deque([row[-1] for row in rc])        # 오른쪽 열
    middle = deque([deque(row[1:-1]) for row in rc])  # 가운데 부분

    for op in operations:
        if op == "ShiftRow":
            # 마지막 행을 맨 앞으로 이동
            left.appendleft(left.pop())
            right.appendleft(right.pop())
            middle.appendleft(middle.pop())
            
        elif op == "Rotate":
            # 회전 순서: 왼쪽 위 → 오른쪽 위 → 오른쪽 아래 → 왼쪽 아래
            top = middle[0]
            bottom = middle[-1]
            
            # 위쪽 행 오른쪽으로 밀기
            top.appendleft(left.popleft())
            right.appendleft(top.pop())
            
            # 아래쪽 행 왼쪽으로 밀기
            bottom.append(right.pop())
            left.append(bottom.popleft())

    # 최종 행렬 재조합
    result = []
    for i in range(n):
        result.append([left[i]] + list(middle[i]) + [right[i]])
    return result