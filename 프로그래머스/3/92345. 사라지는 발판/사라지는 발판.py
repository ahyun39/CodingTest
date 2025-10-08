def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(r1, c1, r2, c2):
            
        # 현재 플레이어가 움직일 수 있는지 확인
        can_move = False
        for dx, dy in dirs:
            nx, ny = r1 + dx, c1 + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                can_move = True
                break
        if not can_move or board[r1][c1] == 0:
            return (False, 0)
        
        win_turns = []
        lose_turns = []
        
        for dx, dy in dirs:
            nx, ny = r1 + dx, c1 + dy
            if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] == 0:
                continue
            board[r1][c1] = 0
            is_win, turn_cnt = dfs(r2, c2, nx, ny)
            board[r1][c1] = 1
            
            if not is_win: # 상대방이 졌다면, 나는 이긴 것
                win_turns.append(turn_cnt + 1)
            else:
                lose_turns.append(turn_cnt + 1)
        if win_turns:
            return (True, min(win_turns))
        else:
            return (False, max(lose_turns))
    _, turn_cnt = dfs(aloc[0], aloc[1], bloc[0], bloc[1])
    
    return turn_cnt