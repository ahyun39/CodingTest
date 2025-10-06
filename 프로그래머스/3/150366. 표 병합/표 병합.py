from collections import defaultdict

def solution(commands):
    excel = [["EMPTY" for _ in range(51)] for _ in range(51)]
    parent = {(r, c): (r, c) for r in range(51) for c in range(51)}  # 병합 관계 관리
    answer = []

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa == pb:
            return
        # 병합 시 값 선택
        val_a, val_b = excel[pa[0]][pa[1]], excel[pb[0]][pb[1]]
        new_val = val_a if val_a != "EMPTY" else val_b
        excel[pa[0]][pa[1]] = excel[pb[0]][pb[1]] = new_val
        parent[pb] = pa  # 병합 방향 설정

    def update_all(value1, value2):
        for i in range(1, 51):
            for j in range(1, 51):
                if excel[i][j] == value1:
                    excel[i][j] = value2

    def unmerge(r, c):
        root = find((r, c))
        saved_val = excel[root[0]][root[1]]
        # 같은 그룹의 셀들 찾기
        merged = [k for k, v in parent.items() if find(v) == root]
        for cell in merged:
            parent[cell] = cell
            excel[cell[0]][cell[1]] = "EMPTY"
        excel[r][c] = saved_val

    for command in commands:
        cmd = command.split()
        if cmd[0] == "UPDATE":
            if len(cmd) == 4:
                r, c, value = int(cmd[1]), int(cmd[2]), cmd[3]
                root = find((r, c))
                excel[root[0]][root[1]] = value
            else:
                update_all(cmd[1], cmd[2])
        elif cmd[0] == "MERGE":
            r1, c1, r2, c2 = map(int, cmd[1:])
            union((r1, c1), (r2, c2))
        elif cmd[0] == "UNMERGE":
            r, c = int(cmd[1]), int(cmd[2])
            unmerge(r, c)
        elif cmd[0] == "PRINT":
            r, c = int(cmd[1]), int(cmd[2])
            root = find((r, c))
            answer.append(excel[root[0]][root[1]])

    return answer