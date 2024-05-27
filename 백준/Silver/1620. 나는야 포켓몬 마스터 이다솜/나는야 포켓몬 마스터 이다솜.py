n, m = map(int,input().split())
monster_dict = {}
monsters = [0]
for i in range(n):
    monster = str(input())
    monster_dict[monster] = (i+1)
    monsters.append(monster)
for i in range(m):
    input_ = str(input())
    if input_.isalpha():
        print(monster_dict[input_])
    else:
        print(monsters[int(input_)])