def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            days.append(int((100-progresses[i]) // speeds[i]))
        else:
            days.append(int((100-progresses[i]) // speeds[i])+1)

    while len(days) > 0: 
        s = days.pop(0)
        out = 1        
        if len(days) == 0:
            answer.append(out)
            break
        else: 
            while days[0] <= s:
                out += 1
                days.pop(0)
                if len(days) == 0:
                    break
        answer.append(out)
        
    return answer