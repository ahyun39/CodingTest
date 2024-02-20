s = list(str(input()))
ans = 'z'*50
for i in range(1,len(s)-1):
    for j in range(i+1,len(s)):
        a, b, c = list(reversed(s[:i])), list(reversed(s[i:j])), list(reversed(s[j:]))
        ans = min(ans,''.join(a+b+c))
print(ans)