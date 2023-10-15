def solution(n, words):
    idx = 1
    used = []
    while True:
        if len(words) == 0:
            return [0,0]
            
        for p in range(1,n+1):
            if len(words) == 0:
                break                
            word = words.pop(0)
            if used:
                if word in used:
                    return [p, idx]
                if word[0] != used[-1][-1]:
                    return [p, idx]
            used.append(word)
        
        idx += 1
    
    return [0,0]