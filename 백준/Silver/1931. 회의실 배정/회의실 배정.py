N = int(input())
meetings = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:(x[1],x[0]))
ans = 0
end = 0
for meeting in meetings:
    if end <= meeting[0]:
        end = meeting[1]
        ans += 1
print(ans)