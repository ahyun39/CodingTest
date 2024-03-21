from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for permu in permutations(dungeons,len(dungeons)):
        fatigue = k
        cnt = 0
        for p in permu:
            if fatigue >= p[0]:
                fatigue -= p[1]
                cnt += 1
            else:
                break
        if cnt > answer:
            answer = cnt
        if answer == len(dungeons):
            break
    return answer