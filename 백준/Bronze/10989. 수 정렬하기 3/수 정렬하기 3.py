l = [0] * (10001)
for _ in range(int(input())):
    l[int(input())] += 1
for i in range(len(l)):
    if l[i] > 0:
        for j in range(l[i]):
            print(i)