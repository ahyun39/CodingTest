def solution(info, edges):
    n = len(info)
    # 트리를 부모 -> 자식으로 저장 (문제 조건에서 edges는 [parent, child] 형태)
    tree = [[] for _ in range(n)]
    for a, b in edges:
        tree[a].append(b)
    
    ans = 0
    
    # 메모: (visited_mask, tupe(sorted(available)) 형태로 이미 방문한 상태를 저장해 중복 제거)
    seen = set()
    
    # 초기 상태: 루트(0)는 항상 양(문제 조건)
    init_mask = 1 << 0
    init_sheep = 1 # info[0] == 0이므로
    init_wolf = 0
    
    # 초기 available: 루트의 자식들(루트는 이미 방문된 상태)
    init_available = list(tree[0])
    
    def dfs(sheep, wolf, available, mask):
        nonlocal ans
        # 현재까지 모은 양 갱신
        if sheep > ans:
            ans = sheep
        
        # 메모키 (mask와 available의 정규화된 표현)
        key = (mask, tuple(sorted(available)))
        if key in seen:
            return
        seen.add(key)
        
        # available 중 하나씩 선택해서 재귀 탐색
        for i, node in enumerate(list(available)):
            # node는 아직 방문되지 않은 노드여야 함(available 구성상 그럴 것)
            if mask & (1 << node):
                # 이미 방문되었으면 건너뜀 (보수성)
                continue
            # 이 노드를 방문할 때 추가되는 양/늑대 수
            add_sheep = 1 if info[node] == 0 else 0
            add_wolf = 1 if info[node] == 1 else 0
            
            ns = sheep + add_sheep
            nw = wolf + add_wolf
            
            # 만약 획득 후 늑대가 양 이상이면 양이 잡아먹히므로 실패 분기
            if nw >= ns:
                continue
            
            # 방문 처리: 이 노드를 visited로 바꿈
            nmask = mask | (1 << node)
            
            # 새로운 available: 현재 available에서 node 제거, node의 자식들을 추가
            navail = available.copy()
            navail.remove(node)
            for child in tree[node]:
                # child가 아직 방문되지 않았다면 추가
                if not (nmask & (1 << child)):
                    navail.append(child)
            
            # 재귀
            dfs(ns, nw, navail, nmask)
    dfs(init_sheep, init_wolf, init_available, init_mask)
    
    return ans