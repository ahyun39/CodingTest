def solution(s):
    answer = 0
    sList = []
    lenList = []
    for i in range(1,len(s)//2+1):
        cutList = [] # 압축된 문자를 담은 리스트
        sameList = [] # 단위별로 자른 문자의 개수를 찾기 위한 리스트
        for k in range(0,len(s),i):
            if s[k:k+i] not in sameList: # 현재 문자가 sameList에 없으면
                sameList = [s[k:k+i]]
                if s[k:k+i] != s[k+i:k+i+i]: # 다음 문자랑 현재 문자랑 다른 경우
                    cutList.append(s[k:k+i])
            elif (s[k:k+i] in sameList) and (s[k:k+i] != s[k+i:k+i+i]): # 현재 문자가 sameList에 있으면서 다음 문자가 현재 문자랑 다른 경우
                sameList.append(s[k:k+i]) # sameList에 추가
                cutList.append(str(sameList.count(s[k:k+i]))+s[k:k+i]) # 압축된 문자 구하기
            elif (s[k:k+i] in sameList) and (s[k:k+i] == s[k+i:k+i+i]): # 현재 문자가 sameList에 있으면서 다음 문자가 현재 문자랑 같은 경우
                sameList.append(s[k:k+i]) # sameList에 추가
        sList.append(''.join(cutList)) # 압축된 문자를 합쳐서 문자열로 join해서 sList에 저장
    for i in sList:
        lenList.append(len(i))
    if len(s) == 1:
        answer = 1
    else:
        answer = min(lenList)
    return answer