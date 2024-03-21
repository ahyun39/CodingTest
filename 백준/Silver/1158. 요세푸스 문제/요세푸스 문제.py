n, k = map(int,input().split())
people = [i+1 for i in range(n)]
output = []
while people:
    if len(people) >= k:
        out = people[k-1]
        after = people[k:] + people[:k-1]
        people = after
    else:
        out = people[(k-1)%len(people)]
        idx = (k-1)%len(people)
        after = people[idx+1:] + people[:idx]
        people = after
    output.append(out)
print(str(output).replace('[','<').replace(']','>'))