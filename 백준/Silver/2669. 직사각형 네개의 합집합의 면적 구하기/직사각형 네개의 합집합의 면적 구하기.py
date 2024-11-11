four_squares = [list(map(int,input().split())) for _ in range(4)]
area = [[0] * 100 for _ in range(100)]

for square in four_squares:
    lx, ly, rx, ry = square
    for i in range(ly, ry):
        for j in range(lx, rx):
            area[i][j] = 1

result = 0
for a in area:
    result += sum(a)
print(result)