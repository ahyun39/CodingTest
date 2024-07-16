def solution(babbling):
    # 발음 가능한 문자열 리스트
    can_babble = ["aya", "ye", "woo", "ma"]
    
    # 유효한 단어의 개수를 저장할 변수
    valid_count = 0
    
    # 각 문자열에 대해 검사
    for word in babbling:
        original_word = word
        for babble in can_babble:
            # 같은 발음이 연속해서 나오지 않도록 수정
            if babble * 2 not in word:
                word = word.replace(babble, " ")
        
        # 모든 발음을 공백으로 대체했을 때 남는 것이 없어야 유효한 단어
        if word.strip() == "":
            valid_count += 1
    
    return valid_count
