n = int(input())
nn = [list(map(str,input().split())) for _ in range(n)]

m = int(input())
mm = [list(map(str,input().split())) for _ in range(m)]

tf = {}
for s in nn:
    tf[s[0]] = s[2]
for s in mm:
    a = s[0]
    b = s[2]
    while a in tf:
        a = tf[a]
        if a == b:
            break
    if a == b:
        print("T")
    else:
        print("F")