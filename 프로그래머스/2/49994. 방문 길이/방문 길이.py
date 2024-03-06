def solution(dirs):
    answer = 0
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    x, y = 0, 0
    lanes = []

    for d in dirs:
        dx, dy = directions[int(d.replace("U","0").replace("D","1").replace("R","2").replace("L","3")) % 4]
        if -5 <= x + dx <= 5 and -5 <= y + dy <= 5:
            nx, ny = x + dx, y + dy
            if (x, y, nx, ny) not in lanes and (nx, ny, x, y) not in lanes:
                answer += 1
                lanes.append((x, y, nx, ny))
            x, y = nx, ny
    return answer