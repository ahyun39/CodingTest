from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

players = list(range(n))
min_diff = float('inf')

for c in combinations(players, n // 2):
    team_a = list(c)
    team_b = [i for i in players if i not in team_a]
    team_a_score = 0
    team_b_score = 0
    
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            team_a_score += s[team_a[i]][team_a[j]] + s[team_a[j]][team_a[i]]
            team_b_score += s[team_b[i]][team_b[j]] + s[team_b[j]][team_b[i]]
    
    diff = abs(team_a_score - team_b_score)
    if diff < min_diff:
        min_diff = diff
    
    if min_diff == 0:
        break

print(min_diff)