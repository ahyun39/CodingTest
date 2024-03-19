from itertools import combinations

def solution(orders, course):
    answer = []
    for n in course:
        set_menu = {}
        for order in orders:
            order = ''.join(sorted(list(order)))
            for c in combinations(order,n):
                menu = ''.join(c)
                set_menu[menu] = set_menu.get(menu,0) + 1
        answer += [k for k,v in set_menu.items() if max(set_menu.values()) == v and v >= 2]
    answer.sort()
    return answer