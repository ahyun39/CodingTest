def solution(name, yearning, photo):
    answer = []
    picture_dict = dict(zip(name,yearning))
    for i in photo:
        s = sum([picture_dict.get(j,0) for j in i])
        answer.append(s)
    return answer