def solution(elements):
    s = set(elements)
    l = len(elements)
    elements = elements + elements + elements
    for i in range(1,l):
        for j in range(i,l+i):
            s.add(sum(elements[j-i:j+1]))
    return len(s)