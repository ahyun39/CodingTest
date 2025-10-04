def solution(friends, gifts):
    answer = 0
    next_month_gift = []
    gift_record = {friend:{friend:0 for friend in friends} for friend in friends}
    gift_cnt = {friend:0 for friend in friends}
    
    for gift in gifts:
        give, receive = map(str, gift.split())
        gift_record[give][receive] += 1
        gift_cnt[give] += 1
        gift_cnt[receive] -= 1
    
    for friend in friends:
        give_take = gift_record[friend]
        cnt = 0
        for f in friends:
            if friend != f:
                if give_take[f] > gift_record[f][friend]:
                    cnt += 1
                elif give_take[f] == gift_record[f][friend]:
                    if gift_cnt[friend] > gift_cnt[f]:
                        cnt += 1
        next_month_gift.append(cnt)

    return max(next_month_gift)