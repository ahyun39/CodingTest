n = int(input())
members = []
for i in range(n):
    age, name = map(str,input().split())
    members.append((i,int(age),name))
members.sort(key=lambda x:(x[1],x[0]))
for member in members:
    print(*member[1:])