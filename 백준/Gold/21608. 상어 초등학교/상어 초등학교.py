# git commit -m "[BOJ] 21608_상어 초등학교 / 골드5 / 90분 / X" 60
# https://www.acmicpc.net/problem/21608

n = int(input())
class_room = [[0 for _ in range(n)] for _ in range(n)]
friends = []
sit = []

for _ in range(n*n):
    student = list(map(int,input().split()))
    friends.append(student)

def friend_seat(friendss):
    who = []
    for f in friendss:
        if f in sit:
            who.append(f)
    return who

for friend in friends:
    if sit == []: 
        class_room[1][1] = friend[0]
        sit.append(friend[0])
    else:
        sit.append(friend[0])
        who = friend_seat(friend[1:])
        if who != []:
            max_like = 0
            max_empty = 0
            seat_i, seat_j = 0, 0
            for i in range(n):
                for j in range(n):
                    like = 0
                    empty = 0
                    if class_room[i][j] == 0:
                        if i-1 >= 0 and class_room[i-1][j] in who: like += 1
                        if j-1 >= 0 and class_room[i][j-1] in who: like += 1
                        if i+1 < n and class_room[i+1][j] in who: like += 1
                        if j+1 < n and class_room[i][j+1] in who: like += 1

                        if i-1 >= 0 and class_room[i-1][j] == 0: empty += 1
                        if j-1 >= 0 and class_room[i][j-1] == 0: empty += 1
                        if i+1 < n and class_room[i+1][j] == 0: empty += 1
                        if j+1 < n and class_room[i][j+1] == 0: empty += 1

                        if max_like < like:
                            max_like = like
                            seat_i, seat_j = i, j
                            max_empty = empty
                        elif max_like == like:
                            if max_empty < empty:
                                max_empty = empty
                                seat_i, seat_j = i, j
                            elif max_empty == empty:
                                if class_room[seat_i][seat_j] != 0:
                                    seat_i, seat_j = i, j
                        
            class_room[seat_i][seat_j] = friend[0]
        elif who == []:
            max_empty = 0
            seat_i, seat_j = 0, 0
            for i in range(n):
                for j in range(n):
                    empty = 0
                    if class_room[i][j] == 0:
                        if i-1 >= 0 and class_room[i-1][j] == 0: empty += 1
                        if j-1 >= 0 and class_room[i][j-1] == 0: empty += 1
                        if i+1 < n and class_room[i+1][j] == 0: empty += 1
                        if j+1 < n and class_room[i][j+1] == 0: empty += 1
                        if max_empty < empty:
                            max_empty = empty
                            seat_i, seat_j = i, j
                        elif max_empty == empty:
                            if class_room[seat_i][seat_j] != 0:
                                seat_i, seat_j = i, j
            class_room[seat_i][seat_j] = friend[0]

answer = 0
for i in range(n):
    for j in range(n):
        near_friend = 0
        near = []
        for friend in friends:
            if friend[0] == class_room[i][j]:
                near = friend[1:]
                break
        if i-1 >= 0 and class_room[i-1][j] in near: near_friend += 1
        if j-1 >= 0 and class_room[i][j-1] in near: near_friend += 1
        if i+1 < n and class_room[i+1][j] in near: near_friend += 1
        if j+1 < n and class_room[i][j+1] in near: near_friend += 1

        if near_friend == 1: answer += 1
        elif near_friend == 2: answer += 10
        elif near_friend == 3: answer += 100
        elif near_friend == 4: answer += 1000
print(answer)