import math

def solution(fees, records):
    answer = []
    #fees : 기본 시간, 기본 요금, 단위 시간, 단위 요금
    car_parking_time = {}
    in_out = []
    total_parking_time = {}
    for record in records:
        time, car, in_or_out = map(str,record.split())
        if in_or_out == "IN":
            in_out.append(car)
            start_time = int(time[0:2])*60 + int(time[3:])
            car_parking_time[car] = start_time
        else:
            in_out.remove(car)
            end_time = int(time[0:2])*60 + int(time[3:])
            car_parking_time[car] = end_time - car_parking_time[car]
            if car in total_parking_time.keys():
                total_parking_time[car] += car_parking_time[car]
            elif car not in total_parking_time.keys():
                total_parking_time[car] = car_parking_time[car]
    print(car_parking_time)
    if in_out:
        for car in in_out:
            end_time = 23*60 + 59
            car_parking_time[car] = end_time - car_parking_time[car]
            if car in total_parking_time.keys():
                total_parking_time[car] += car_parking_time[car]
            elif car not in total_parking_time.keys():
                total_parking_time[car] = car_parking_time[car]
    car_total_time = sorted(total_parking_time.items(),key=lambda x:x[0])
    for total_time in car_total_time:
        if total_time[1] <= fees[0]: answer.append(fees[1])
        else:
            fee = fees[1] + math.ceil((total_time[1] - fees[0])/fees[2]) * fees[3]
            answer.append(fee)

    return answer