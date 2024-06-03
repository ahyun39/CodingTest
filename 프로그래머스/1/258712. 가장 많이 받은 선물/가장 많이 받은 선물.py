def solution(friends, gifts):
    answer = 0
    n = len(friends)
    give_and_take = [[0]*n for _ in range(n)]
    for gift in gifts:
        a, b = map(str,gift.split())
        give_and_take[friends.index(a)][friends.index(b)] += 1
    gift_level = {}
    for i in range(n):
        p_give = sum(give_and_take[i])
        p_receive = sum([give_and_take[j][i] for j in range(n)])
        gift_level[friends[i]] = p_give - p_receive
    for i in range(n):
        cnt = 0
        f = friends[i] # 대상 캐릭터
        for j in range(n):
            if i != j:
                if give_and_take[i][j] > give_and_take[j][i]:
                    cnt += 1
                if give_and_take[i][j] == give_and_take[j][i]:
                    if gift_level[f] > gift_level[friends[j]]:
                        cnt += 1
        if answer < cnt:
            answer = cnt
            
    return answer