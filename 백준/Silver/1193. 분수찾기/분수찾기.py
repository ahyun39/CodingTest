x = int(input())

i = 1
t = 0
ans = [0,0]
while True:
    if t == x: break
    if i % 2 == 0:
        for j in range(i):
            ans = [j+1,i-j]
            t += 1
            if t == x: break
    elif i % 2 == 1:
        for j in range(i):
            ans = [i-j,j+1]
            t += 1
            if t == x: break
    i += 1
print('%d/%d'%(ans[0],ans[1]))