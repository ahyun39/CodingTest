from collections import deque

def solution(coin, cards):
    n = len(cards)
    target = n + 1
    hand = cards[:n//3]
    deck = deque(cards[n//3:])
    keep = []  # 뽑았지만 아직 손에 넣지 않은 카드들
    round_cnt = 1

    while deck:
        # 카드 2장 뽑기
        draw = [deck.popleft() for _ in range(min(2, len(deck)))]
        keep.extend(draw)

        # 현재 카드에서 만들 수 있는지 확인
        def can_next(hand):
            for x in hand:
                if target - x in hand:
                    return x, target - x
            return None
        
        # 카드만으로 가능한지
        if can_next(hand):
            a, b = can_next(hand)
            hand.remove(a)
            hand.remove(b)
            round_cnt += 1
            continue
        
        # 카드 + 보류 카드 (코인 1개 사용)
        used = False
        if coin >= 1:
            for x in list(keep):
                if target - x in hand:
                    keep.remove(x)
                    coin -= 1
                    hand.remove(target - x)
                    used = True
                    round_cnt += 1
                    break
            if used:
                continue
        
        # 보류 카드끼리 (코인 2개 사용)
        if coin >= 2:
            for x in list(keep):
                if target - x in keep and x != target - x:
                    keep.remove(x)
                    keep.remove(target - x)
                    coin -= 2
                    round_cnt += 1
                    used = True
                    break
            if used:
                continue
        
        # 더 이상 진행 불가
        break
    
    return round_cnt