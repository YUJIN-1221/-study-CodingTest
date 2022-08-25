def solution(priorities, location):
    loc = location
    ans = 0
    while True:
        s = priorities.pop(0)
        if any([e > s for e in priorities]):
            priorities.append(s)
            if loc == 0:
                loc = len(priorities)-1
            else:
                loc -= 1
        else:
            ans += 1
            if loc == 0:
                return ans                
            else:
                loc -= 1
    
    
    
    
    
    answer = 0
    return answer