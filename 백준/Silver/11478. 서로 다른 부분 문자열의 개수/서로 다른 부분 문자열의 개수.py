s = str(input())
l = []
for i in range(1,len(s)+1):
    for j in range(len(s)-i+1):
        l.append(s[j:j+i])
temp = set(l)
print(len(list(temp)))