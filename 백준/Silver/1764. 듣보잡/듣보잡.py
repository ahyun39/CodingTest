n, m = map(int,input().split())
names = {}
for _ in range(n):
    person = str(input())
    names[person] = names.get(person,0) + 1
for _ in range(m):
    person = str(input())
    names[person] = names.get(person,0) + 1
ans = []
for key, value in names.items():
    if value == 2: ans.append(key)
ans.sort()
print(len(ans))
for a in ans:
    print(a)