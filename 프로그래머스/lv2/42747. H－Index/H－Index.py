def solution(citations):
    if sum(citations) == 0:
        return 0
    
    citations = sorted(citations)
    h = len(citations)
    while h >= 0:
        if citations[len(citations)-h] >= h:
            return h
        else:
            h -= 1