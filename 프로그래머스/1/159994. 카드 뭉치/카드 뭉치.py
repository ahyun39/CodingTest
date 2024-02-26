from collections import deque
def solution(cards1, cards2, goal):
    cards1, cards2 = deque(cards1), deque(cards2)
    for s in goal:
        if s in cards1:
            if cards1[0] == s: cards1.popleft()
            else: return "No"
        if s in cards2:
            if cards2[0] == s: cards2.popleft()
            else: return "No"
    return "Yes"