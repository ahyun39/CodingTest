def solution(n, k):
    turnTok = int(str(n),10)
    str_n = ''
    answer = 0
    while turnTok > 0:
        turnTok, b = divmod(turnTok,k)
        str_n += str(b)
    str_n = str_n[::-1]
    str_list = list(str_n.split('0'))
    for i in range(len(str_list)):
        a = 0
        if str_list[i] != "":
            for t in range(2,int(int(str_list[i])**0.5)+1):
                if int(str_list[i]) % t == 0:
                    a += 1
            if a == 0:
                answer += 1
    answer = answer - str_list.count('1')
    return answer