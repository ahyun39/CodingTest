def f():
    N1 = int(input())
    ynum = set(map(int, input().split()))
    N2 = int(input())
    dnum = list(map(int, input().split()))
    for num in dnum:
        print(1 if num in ynum else 0)

def solution():
    T = int(input())
    for _ in range(T):
        f()

solution()