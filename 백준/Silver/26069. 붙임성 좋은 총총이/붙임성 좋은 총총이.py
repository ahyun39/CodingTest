n = int(input())
rainbowdance = set(["ChongChong"])
ans = 0
for _ in range(n):
    a, b = map(str,input().split())
    if a in rainbowdance:
        rainbowdance.add(b)
    elif b in rainbowdance:
        rainbowdance.add(a)
print(len(rainbowdance))