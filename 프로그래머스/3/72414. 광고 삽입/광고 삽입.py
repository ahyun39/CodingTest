def solution(play_time, adv_time, logs):
    def to_sec(time_str):
        h, m, s = map(int, time_str.split(":"))
        return h * 3600 + m * 60 + s
    
    def to_time_str(sec):
        h = sec // 3600
        sec %= 3600
        m = sec // 60
        s = sec % 60
        return f"{h:02d}:{m:02d}:{s:02d}"
    
    play_time_sec = to_sec(play_time)
    adv_time_sec = to_sec(adv_time)
    
    # 시청자 시작/끝 시간 표시
    timeline = [0] * (play_time_sec + 2)
    for log in logs:
        start, end = log.split("-")
        start, end = to_sec(start), to_sec(end)
        timeline[start] += 1
        timeline[end] -= 1
    
    # 초당 시청자 수 누적합
    for i in range(1, play_time_sec + 1):
        timeline[i] += timeline[i-1]
    
    # 누적 재생 시간 (prefix sum)
    for i in range(1, play_time_sec + 1):
        timeline[i] += timeline[i-1]
    
    # 광고 구간별 시청자 합 계산
    max_watch = timeline[adv_time_sec - 1]
    max_start = 0
    for start in range(adv_time_sec, play_time_sec):
        watch_time = timeline[start] - timeline[start - adv_time_sec]
        if watch_time > max_watch:
            max_watch = watch_time
            max_start = start - adv_time_sec + 1
    return to_time_str(max_start)