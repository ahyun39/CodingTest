from collections import deque
n = int(input()) # 사진틀의 개수
m = int(input()) # 추천 횟수
recommends = list(map(int,input().split())) # 추천받은 학생
candidates = {}
pictures = deque()
for recommend in recommends:
    candidates[recommend] = candidates.get(recommend,0) + 1
    if recommend not in pictures:
        no_picture = 0
        for i in range(n):
            if len(pictures) < n:
                pictures.append(recommend)
                no_picture = 1
                break
        if no_picture == 0:
            cnt = 1000
            now = 0
            for i in range(n):
                if cnt > candidates[pictures[i]]:
                    cnt = candidates[pictures[i]]
                    now = pictures[i]
            candidates[now] = 0
            pictures.remove(now)
            pictures.append(recommend)
print(*sorted(list(pictures)))