def solution(m, musicinfos):
    answer = ''
    musicinfos = [list(map(str,i.replace("C#","H").replace("D#","I").replace("F#","J").replace("G#","K").replace("A#","L").replace("B#","M").split(","))) for i in musicinfos]
    m = m.replace("C#","H").replace("D#","I").replace("F#","J").replace("G#","K").replace("A#","L").replace("B#","M")
    play = 0

    for info in musicinfos:
        start_time = int(info[0][:2]) * 60 + int(info[0][3:])
        end_time = int(info[1][:2]) * 60 + int(info[1][3:])
        time = end_time - start_time

        music = info[3]*(time//len(info[3])) + info[3][:int(time % len(info[3]))]
        if m in music and time > play:
            answer = info[2]
            play = time
    if answer == '': answer = '(None)'
    return answer