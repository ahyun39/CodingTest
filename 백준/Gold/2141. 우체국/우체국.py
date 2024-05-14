n = int(input())
towns = [list(map(int, input().split())) for _ in range(n)]
towns.sort()

total_population = sum(town[1] for town in towns)
half_population = total_population / 2

current_population = 0
for town in towns:
    current_population += town[1]
    if current_population >= half_population:
        print(town[0])
        break
