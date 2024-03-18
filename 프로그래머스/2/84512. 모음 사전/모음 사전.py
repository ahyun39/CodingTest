from itertools import product
def solution(word):
    answer = 0
    alphabets = ["A", "E", "I", "O", "U"]
    words = ["".join(j) for i in range(1,6) for j in list(product(alphabets,repeat = i))]
    words.sort()
    return words.index(word)+1