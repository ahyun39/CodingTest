def solution(friends, gifts):
    from collections import defaultdict

    gift_record = {f: defaultdict(int) for f in friends}
    gift_cnt = {f: 0 for f in friends}

    # 선물 기록 업데이트
    for gift in gifts:
        give, receive = gift.split()
        gift_record[give][receive] += 1
        gift_cnt[give] += 1
        gift_cnt[receive] -= 1

    next_month_gift = []
    
    # 다음 달 예상 선물 수 계산
    for friend in friends:
        cnt = sum(
            1
            for f in friends
            if f != friend and (
                gift_record[friend][f] > gift_record[f][friend] or
                (gift_record[friend][f] == gift_record[f][friend] and gift_cnt[friend] > gift_cnt[f])
            )
        )
        next_month_gift.append(cnt)

    return max(next_month_gift)