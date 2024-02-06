from itertools import combinations

def calculate_score(team, ability):
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            score += ability[team[i]][team[j]] + ability[team[j]][team[i]]
    return score

N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
player = [i for i in range(N)]
ans = float('inf')

for i in range(1, N // 2 + 1):
    for team_a in combinations(player, i):
        team_b = tuple(x for x in player if x not in team_a)
        
        score_a = calculate_score(team_a, ability)
        score_b = calculate_score(team_b, ability)

        diff = abs(score_a - score_b)
        ans = min(ans, diff)

print(ans)