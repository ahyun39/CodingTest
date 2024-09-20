from itertools import combinations, product
from collections import Counter

def select_dice(dice_num):
    a_dice, b_dice = [], []
    half_len = len(dice_num) // 2
    for c in combinations(dice_num, half_len):
        c = list(c)
        a_dice.append(c)
        b_dice.append([num for num in dice_num if num not in c])
    return a_dice, b_dice

def cal_score(a_score, b_score):
    win, draw, lose = 0, 0, 0
    a_count = Counter(a_score)
    b_count = Counter(b_score)
    
    for a_val in a_count:
        for b_val in b_count:
            if a_val > b_val:
                win += a_count[a_val] * b_count[b_val]
            elif a_val == b_val:
                draw += a_count[a_val] * b_count[b_val]
            else:
                lose += a_count[a_val] * b_count[b_val]
                
    return win / (win + draw + lose)

def roll_dice(a_dice, b_dice, dice_dict):
    max_score = 0
    best_dice = []
    
    for i in range(len(a_dice)):
        a = [dice_dict[x] for x in a_dice[i]]
        b = [dice_dict[x] for x in b_dice[i]]
        
        a_score = [sum(x) for x in product(*a)]
        b_score = [sum(x) for x in product(*b)]
        
        current_score = cal_score(a_score, b_score)
        if current_score > max_score:
            max_score = current_score
            best_dice = a_dice[i]
    
    return best_dice

def solution(dice):
    dice_num = list(range(1, len(dice) + 1))
    a_dice, b_dice = select_dice(dice_num)
    dice_dict = {i + 1: dice[i] for i in range(len(dice))}
    
    return roll_dice(a_dice, b_dice, dice_dict)