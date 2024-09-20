from itertools import combinations

def select_dice(dice_num):
    a_dice, b_dice = [], []
    for c in combinations(dice_num, max(dice_num)//2):
        a_dice.append(list(c))
        b_dice.append([d for d in dice_num not in c])
    return a_dice, b_dice

def solution(dice):
    answer = []
    return answer