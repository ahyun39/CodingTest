def solution(n, arr1, arr2):
    answer = []
    bin_map = []
    for i in range(n):
        to_bin = str(bin(arr1[i] | arr2[i])).replace('b','')[-n:].replace('1','#').replace('0',' ')
        bin_to_str = ' '*(n-len(to_bin)) + to_bin
        answer.append(bin_to_str)
    return answer