from bisect import bisect_left, bisect_right

def binary_search(points, line):
    left, right = line
    lidx = bisect_left(points, left)
    ridx = bisect_right(points, right)
    return ridx - lidx

def f():
    N, M = map(int, input().split())
    points = list(map(int, input().split()))
    points.sort()
    lines = [list(map(int, input().split())) for _ in range(M)]
    
    for line in lines:
        print(binary_search(points, line))
        
f()