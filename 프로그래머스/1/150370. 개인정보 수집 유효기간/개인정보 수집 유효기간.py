from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    # 문자열 -> 날짜 형식으로 변환
    today = datetime.strptime(today, "%Y.%m.%d")
    # 약관 보관 일자 딕셔너리
    term_dict = {term_nm: int(month)*28 for term_nm, month in (term.split() for term in terms)}
    
    for i in range(len(privacies)):
        date, term = map(str, privacies[i].split())
        date = datetime.strptime(date, "%Y.%m.%d")
        month_diff = ((today.year - date.year) * 12 + (today.month - date.month)) * 28 + (today.day - date.day)
        if month_diff >= term_dict[term]:
            answer.append(i+1)
    return answer