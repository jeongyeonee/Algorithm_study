# 버스 도착 시간을 for문으로
# 탑승 가능 인원과 현재 탑승 인원 수 비교하여 진행

def solution(n, t, m, timetable):
    timetable = sorted([int(time[:2])*60 + int(time[3:]) for time in timetable])
    bus_time = [9*60 + i*t for i in range(n)]
    i = 0 # timetable's index
    for bus in bus_time:
        cnt = 0 # 현재 탑승 인원
        while i < len(timetable) and timetable[i] <= bus and cnt < m :
            i += 1
            cnt += 1
            print(i, cnt)
        if cnt < m:
            answer = bus
        else:
            answer = timetable[i-1] - 1
    return str(answer//60).zfill(2)+':'+str(answer%60).zfill(2)
  
 
