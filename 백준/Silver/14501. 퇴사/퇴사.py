N = int(input())
counsel = [list(map(int, input().split())) for _ in range(N)]

def recur(idx, price):
    global answer

    if idx == N:
        answer = max(answer, price)
        return answer
    if idx > N:
        return

    recur(idx + counsel[idx][0], price + counsel[idx][1])
    recur(idx+1, price)

answer = 0
recur(0, 0)
print(answer)