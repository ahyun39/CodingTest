n = int(input())
time_n = list(map(int,input().split()))
time_n = sorted(time_n)
answer = 0
for i in range(n):
    take_time = 0
    for j in range(i+1):
        take_time += time_n[j]
    answer += take_time
print(answer)