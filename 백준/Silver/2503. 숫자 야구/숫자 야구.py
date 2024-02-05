from itertools import permutations

N = int(input())
items = [str(i) for i in range(1,10)]
ans = 0
it = []
for i in range(N):
    num, strike, ball = map(int,input().split())
    it.append([num, strike, ball])

all_num = list(permutations(list(items),3))

def baseball(num, it):
    for i in range(len(it)):
        strike, ball = 0, 0
        guess = list(str(it[i][0]))
        if num[0] in guess:
            if (guess[0] == num[0]): strike += 1
            else: ball += 1
        if num[1] in guess:
            if (guess[1] == num[1]): strike += 1
            else: ball += 1
        if num[2] in guess:
            if (guess[2] == num[2]): strike += 1
            else: ball += 1
        if strike != it[i][1] or ball != it[i][2]: return False
    return True

for num in all_num:
    if baseball(num, it):
        ans += 1
print(ans)