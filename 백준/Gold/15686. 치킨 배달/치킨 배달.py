# 15686_치킨 배달_골드5

from itertools import combinations

def f():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    chickens = [(i+1, j+1) for i in range(N) for j in range(N) if board[i][j] == 2]
    houses = [(i+1, j+1) for i in range(N) for j in range(N) if board[i][j] == 1]

    min_dist = float('inf')

    for c in combinations(chickens, M):
        dist = 0
        for house in houses:
            hx, hy = house
            house_to_chicken = 101
            for chicken in c:
                cx, cy = chicken
                d = abs(cx-hx) + abs(cy-hy)
                if house_to_chicken > d:
                    house_to_chicken = d
            dist += house_to_chicken
        if min_dist > dist:
            min_dist = dist
    print(min_dist)

f()