def solution(files):
    answer = []
    split_files = []
    for file in files:
        idx = []
        is_num = 0
        for i in range(len(file)):
            if file[i].isdigit() and is_num == 0:
                is_num = 1
                idx.append(i)
            elif not file[i].isdigit() and is_num == 1:
                idx.append(i)
                break
        if len(idx) > 1:
            split_files.append([file[:idx[0]], file[idx[0]:idx[1]], file[idx[1]:]])
        else:
            split_files.append([file[:idx[0]],file[idx[0]:]])
    split_files = sorted(split_files, key=lambda x:(x[0].lower(),int(x[1]),files.index(''.join(x))))
    answer = [''.join(f) for f in split_files]
    return answer