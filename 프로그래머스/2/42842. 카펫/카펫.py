def solution(brown, yellow):
    col, row = 0, 0
    colors = brown+yellow
    for i in range(brown,0,-1):
        if colors % i == 0:
            if i >= (colors // i) and colors - (i + (i-1) + (colors//i-1) + (colors//i-2)) == yellow: 
                col, row = i, colors // i
    return [col, row]