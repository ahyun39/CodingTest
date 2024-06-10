n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

idx_zero = [b[i] for i in range(n) if a[i] == 0]
idx_zero = c[::-1] + idx_zero
print(*idx_zero[-m:][::-1])