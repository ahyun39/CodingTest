n, k = map(int,input().split())
people = [i for i in range(1,n+1)]
ans = []
t = 0
while people:
    t = (t+k-1) % len(people)
    ans.append(people.pop(t))
output = "<" + ", ".join(str(num) for num in ans) + ">"
print(output)