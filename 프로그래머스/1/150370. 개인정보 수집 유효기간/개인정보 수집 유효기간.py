def solution(today, terms, privacies):
    # 오늘 날짜를 연,월,일로 분리
    t_year, t_month, t_day = map(int, today.split('.'))
    # 약관별 유효기간(일) 딕셔너리
    term_dict = {k: int(v) * 28 for k, v in (t.split() for t in terms)}

    answer = []
    for i, privacy in enumerate(privacies):
        p_date, p_term = privacy.split()
        p_year, p_month, p_day = map(int, p_date.split('.'))
        # 총 일수 계산: 연, 월, 일 단위
        total_days = (t_year - p_year) * 12 * 28 + (t_month - p_month) * 28 + (t_day - p_day)
        if total_days >= term_dict[p_term]:
            answer.append(i + 1)

    return answer