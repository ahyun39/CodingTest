def solution(files):
    split_files = []
    for file in files:
        head, number, tail = "", "", ""
        for i, c in enumerate(file):
            if c.isdigit():
                number += c
            else:
                if number:
                    tail = file[i:]
                    break
                else:
                    head += c
        split_files.append([head, number, tail])
    
    split_files.sort(key=lambda x: (x[0].lower(), int(x[1]), files.index(''.join(x))))
    return [''.join(f) for f in split_files]