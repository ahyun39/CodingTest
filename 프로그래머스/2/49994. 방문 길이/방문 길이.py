def solution(dirs):
    answer = 0
    directions = [[0,1],[0,-1],[1,0],[-1,0]]
    x, y = 0, 0
    lanes = []
    for i in range(len(dirs)):
        if dirs[i] == "U":
            if -5 <= x + directions[0][0] <= 5 and -5 <= y + directions[0][1] <= 5:
                nx, ny = x + directions[0][0], y + directions[0][1]
                if [x, y, nx, ny] not in lanes and [nx, ny, x, y] not in lanes:
                    answer += 1
                    lanes.append([x, y, nx, ny])
                x, y = nx, ny
        elif dirs[i] == "D":
            if -5 <= x + directions[1][0] <= 5 and -5 <= y + directions[1][1] <= 5:
                nx, ny = x + directions[1][0], y + directions[1][1]
                if [x, y, nx, ny] not in lanes and [nx, ny, x, y] not in lanes:
                    answer += 1
                    lanes.append([x, y, nx, ny])
                x, y = nx, ny
        elif dirs[i] == "R":
            if -5 <= x + directions[2][0] <= 5 and -5 <= y + directions[2][1] <= 5:
                nx, ny = x + directions[2][0], y + directions[2][1]
                if [x, y, nx, ny] not in lanes and [nx, ny, x, y] not in lanes:
                    answer += 1
                    lanes.append([x, y, nx, ny])
                x, y = nx, ny
        elif dirs[i] == "L":
            if -5 <= x + directions[3][0] <= 5 and -5 <= y + directions[3][1] <= 5:
                nx, ny = x + directions[3][0], y + directions[3][1]
                if [x, y, nx, ny] not in lanes and [nx, ny, x, y] not in lanes:
                    answer += 1
                    lanes.append([x, y, nx, ny])
                x, y = nx, ny
    return answer