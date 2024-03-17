import copy
def solution(want, number, discount):
    answer = 0
    items = {}
    for a, b in zip(want,number):
        items[a] = b
    for i in range(len(discount)-9):
        items_ = copy.deepcopy(items)
        for j in range(i,i+10):
            if discount[j] in items_.keys():
                items_[discount[j]] = max(items_[discount[j]]-1,0)
            if sum(items_.values()) <= 0:
                answer += 1
    return answer