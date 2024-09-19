def solution(park, routes):
    h, w = len(park), len(park[0])
    for land in park:
        if "S" in land:
            ans = [park.index(land), land.index("S")]
            break
    d_dict = {"N":[-1,0], "S":[1,0], "W":[0,-1], "E":[0,1]}
    
    def check(ans, direct, n):
        x, y = ans
        for i in range(n):
            x += direct[0]
            y += direct[1]
            if park[x][y] == "X":
                return False
        return True
    
    for route in routes:
        op, n = map(str, route.split())
        nx, ny = d_dict[op][0] * int(n) + ans[0], d_dict[op][1] * int(n) + ans[1]
        if 0 <= nx < h and 0 <= ny < w:
            if check(ans, d_dict[op], int(n)):
                ans = [nx, ny]
            
    return ans