from itertools import permutations

def solution(user_id, banned_id):
    def is_match(user, ban):
        if len(user) != len(ban):
            return False
        return all(b == '*' or b == u for b, u in zip(ban, user))

    valid_users = []
    for ban in banned_id:
        valid_users.append([user for user in user_id if is_match(user, ban)])

    all_combinations = set()
    def backtrack(index, chosen_users):
        if index == len(banned_id):
            if len(chosen_users) == len(banned_id):
                all_combinations.add(frozenset(chosen_users))
            return
        
        for user in valid_users[index]:
            if user not in chosen_users:
                chosen_users.add(user)
                backtrack(index + 1, chosen_users)
                chosen_users.remove(user)

    backtrack(0, set())
    
    return len(all_combinations)