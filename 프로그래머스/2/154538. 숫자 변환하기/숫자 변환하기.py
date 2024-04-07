from collections import deque

def solution(x, y, n):
    if x == y: 
        return 0
    
    visited = set()
    queue = deque([(x, 0)])
    
    while queue:
        current, operations = queue.popleft()
        if current == y:
            return operations

        if current < y and current not in visited:
            visited.add(current)
            
            if current + n <= y:
                queue.append((current + n, operations + 1))
            if current * 2 <= y:
                queue.append((current * 2, operations + 1))
            if current * 3 <= y:
                queue.append((current * 3, operations + 1))

    return -1