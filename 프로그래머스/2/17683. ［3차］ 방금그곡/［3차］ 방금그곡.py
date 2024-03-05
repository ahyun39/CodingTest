def solution(m, musicinfos):
    # '#'을 다른 문자로 치환하는 함수
    def replace_sharp(s):
        return s.replace("C#", "H").replace("D#", "I").replace("F#", "J").replace("G#", "K").replace("A#", "L").replace("B#", "M")

    musicinfos = [list(map(str, replace_sharp(i).split(","))) for i in musicinfos]
    m = replace_sharp(m)

    play_time = 0
    play_music = ''

    for info in musicinfos:
        start_time = int(info[0][:2]) * 60 + int(info[0][3:])
        end_time = int(info[1][:2]) * 60 + int(info[1][3:])
        time = end_time - start_time

        music = info[3] * (time // len(info[3])) + info[3][:int(time % len(info[3]))]

        if m in music and time > play_time:
            play_music = info[2]
            play_time = time

    return play_music if play_music else '(None)'
