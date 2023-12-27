sound = list(str(input()))
duck_sound = "quack"
ducks = []
for i in range(1,sound.count("q")+1):
    t = 0
    for s in range(len(sound)):
        if t == 5: t = 0
        if duck_sound[t] == sound[s]:
            sound[s] = i
            t += 1

    if t == 0 and i != sound[-1] and i in sound:
        ducks.append(i)
    elif t == 5 and i == sound[-1]:
        ducks.append(i)
temp = set(sound)
if list(temp) == ducks:
    print(max(ducks))
else:
    print(-1)