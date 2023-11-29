from itertools import combinations
word = str(input())
idx_list = [i for i in range(len(word))]
change_word = []
for i in combinations(idx_list,3):
    # divide to three words
    a, b, c = word[:idx_list[i[0]]+1], word[idx_list[i[0]]+1:idx_list[i[1]]+1], word[idx_list[i[1]]+1:]
    # reverse
    ra, rb, rc = a[::-1], b[::-1], c[::-1]
    change_word.append(ra+rb+rc)
change_word.sort()
print(change_word[0])