t = int(input())
for _ in range(t):
    votes = int(input())
    print('++++ '*(votes // 5) + '|'*(votes % 5))