def solution(msg):
    answer = []
    alpha_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
                 'H':8,'I':9,'J':10,"K":11,'L':12,'M':13,'N':14,
                 'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,
                 'V':22,'W':23,'X':24,'Y':25,'Z':26}
    last_idx = 26
    l = len(msg)
    i = 0
    while i < l:
        start, end = i, i
        while True:
            if end == l - 1:
                if msg[start:end+1] in alpha_dict.keys():
                    answer.append(alpha_dict[msg[start:end+1]])
                    end += 1
                    break
            if msg[start:end+1] not in alpha_dict.keys():
                last_idx += 1
                alpha_dict[msg[start:end+1]] = last_idx 
                answer.append(alpha_dict[msg[start:end]])
                break
            end += 1
        i = end
    return answer