from collections import deque

a, b, c = map(int,input().split())

def water(a,b,c):
    visited = set()
    q = deque([(0,0,c)])
    amounts = set()

    while q:
        x, y, z = q.popleft()
        if (x,y,z) in visited:
            continue
        visited.add((x, y, z))
        if x == 0:
            amounts.add(z)
        # 1번 물통 -> 2번 물통
        if x + y <= b:
            q.append((0, x + y, z))
        else:
            q.append((x - (b - y), b, z))
        # 1번 물통 -> 3번 물통
        if x + z <= c:
            q.append((y + x, 0, z))
        else:
            q.append((a, y - (a - x), z))
        # 2번 물통 -> 1번 물통
        if y + x <= a:
            q.append((y + x, 0, z))
        else:
            q.append((a, y - (a - x), z))
        # 2번 물통 -> 3번 물통
        if y + z <= c:
            q.append((x, 0, y + z))
        else:
            q.append((x, y - (c - z), c))
        # 3번 물통 -> 1번 물통
        if z + x <= a:
            q.append((z + x, y, 0))
        else:
            q.append((a, y, z - (a - x)))
        # 3번 물통 -> 2번 물통
        if z + y <= b:
            q.append((x, z + y, 0))
        else:
            q.append((x, b, z - (b - y)))
    return sorted(amounts)
print(*water(a,b,c))