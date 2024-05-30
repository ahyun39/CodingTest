def solution(s):
    answer = 0
    sList = []
    lenList = []
    for i in range(1,len(s)//2+1):
        cutList = []
        sameList = []
        for k in range(0,len(s),i):
            if s[k:k+i] not in sameList:
                sameList = []
                sameList.append(s[k:k+i])
                if s[k:k+i] != s[k+i:k+i+i]:
                    cutList.append(s[k:k+i])
            elif (s[k:k+i] in sameList) and (s[k:k+i] != s[k+i:k+i+i]):
                sameList.append(s[k:k+i])
                cutList.append(str(sameList.count(s[k:k+i]))+s[k:k+i])
            elif (s[k:k+i] in sameList) and (s[k:k+i] == s[k+i:k+i+i]):
                sameList.append(s[k:k+i])
        sList.append(''.join(cutList))
    for i in sList:
        lenList.append(len(i))
    if len(s) == 1:
        answer = 1
    else:
        answer = min(lenList)
    return answer