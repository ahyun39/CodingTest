n, m = map(int, input().split())
girl_group = {}

for _ in range(n):
    team_name = str(input())
    member_cnt = int(input())
    members = [str(input()) for _ in range(member_cnt)]
    members.sort()
    girl_group[team_name] = members

for _ in range(m):
    name = str(input())
    quiz_type = int(input())
    if quiz_type == 0:
        members = girl_group[name]
        print(*members, sep='\n')
    elif quiz_type == 1:
        team_name = [k for k, v in girl_group.items() if name in v][0]
        print(team_name)