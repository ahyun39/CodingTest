n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
points.sort(key=lambda x:(x[1],x[0]))
for point in points:
    print(*point)