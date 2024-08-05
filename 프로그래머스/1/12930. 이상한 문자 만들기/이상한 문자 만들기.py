def solution(s):
    answer = ''
    ul = "upper"
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            ul = "upper"
        else:
            if ul == "upper":
                answer += s[i].upper()
                ul = "lower"
            else:
                answer += s[i].lower()
                ul = "upper"
    return answer