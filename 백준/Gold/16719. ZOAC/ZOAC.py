word = input()
answer = [word]
if len(word) > 1:
    t = []
    while True:
        if len(word) == 1:
            break
        else:
            for i in range(len(word)):
                t.append(word[:i]+word[i+1:])
            answer.append(min(t))
            word = min(t)
print(*answer[::-1],sep='\n')  