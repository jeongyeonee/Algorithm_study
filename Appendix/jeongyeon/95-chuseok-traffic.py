def solution(lines):
    answer = 0
    start_time, end_time = [], []
    for line in lines:
        s = line.split()[1]
        s = int(s[:2])*60*60 + int(s[3:5])*60 + int(s[6:8]) + float(s[-4:])
        t = float(line.split()[2][:-1])
        start_time.append(round(s-t+0.001, 3))
        end_time.append(s)
    for end in range(len(end_time)):
        cnt = 0
        for start in range(end, len(start_time)):
            if end_time[end] + 1 > start_time[start] :
                cnt += 1
        answer = max(cnt, answer)
    return answer

# 조금 더 코드 간결
# 계산량이 많아질수록 메모리 덜 잡아 먹는 듯
def solution(lines):
    answer = 0
    start_time, end_time = [], []
    for line in lines:
        s = line.split()[1]
        s = int(s[:2])*60*60 + int(s[3:5])*60 + int(s[6:8]) + float(s[-4:])
        t = float(line.split()[2][:-1])
        start_time.append(round(s-t+0.001, 3))
        end_time.append(s)
    for end in range(len(end_time)):
        # 끝나는 시간이 오름차순으로 정렬되어 있기 때문에
        # end_time[end]부터 1초동안 start_time[end:] 들이 실행중인지를 확인.
        cnt = sum([end_time[end] + 1 > st for st in start_time[end:]])
        answer = max(cnt, answer)
    return answer
