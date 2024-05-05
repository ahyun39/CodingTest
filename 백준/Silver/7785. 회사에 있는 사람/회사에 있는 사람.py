n = int(input())
employees = {}
leaves = []
for _ in range(n):
    name, log_ = map(str,input().split())
    if log_ == "enter":
        employees[name] = 1
    else:
        employees[name] = 0
for k, v in employees.items():
    if v == 1:
        leaves.append(k)
leaves.sort(reverse=True)
for p in leaves:
    print(p)