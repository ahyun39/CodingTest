words = [str(input()) for _ in range(int(input()))]
temp = set(words)
words = list(temp)
words.sort(key=lambda x:(len(x),x))
print(*words,sep='\n')