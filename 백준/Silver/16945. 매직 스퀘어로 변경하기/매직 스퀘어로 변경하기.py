import sys
input = sys.stdin.readline

def check(arr):
    left_d = arr[0] + arr[4] + arr[8]
    right_d = arr[2] + arr[4] + arr[6]
    if left_d != 15 or right_d != 15:
        return 0
    row = [0] * 3
    col = [0] * 3
    for i in range(9):
        row[i % 3] += selected[i]
        col[i // 3] += selected[i]
    for i in row:
        if i != 15:
            return 0
    for i in col:
        if i != 15:
            return 0
    return 1


def recur(cur):
    global ans
    if cur == 9:
        if check(selected):
            tmp = 0
            for i in range(9):
                if selected[i] != A[i // 3][i % 3]:
                    tmp += abs(selected[i] - A[i // 3][i % 3])
            ans = min(ans, tmp)
        return
    for i in range(1, 10):
        if visited[i]:
            continue
        visited[i] = 1
        selected[cur] = i
        recur(cur + 1)
        visited[i] = 0


A = [list(map(int, input().split())) for _ in range(3)]
visited = [0] * 10
selected = [0] * 9
ans = 100
recur(0)
print(ans)