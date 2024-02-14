def next_permutation(word):
    n = len(word)
    i = n - 2
    while i >= 0 and word[i] >= word[i + 1]:
        i -= 1
    if i == -1:
        return word
    j = n - 1
    while word[j] <= word[i]:
        j -= 1
    word_list = list(word)
    word_list[i], word_list[j] = word_list[j], word_list[i]
    word_list[i + 1:] = reversed(word_list[i + 1:])
    
    return ''.join(word_list)

T = int(input())
for _ in range(T):
    input_word = input()
    result = next_permutation(input_word)
    print(result)