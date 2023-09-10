def solution(brown, yellow):
    for b in range(brown//4+1, brown//2):
        a = (brown - 2*b)//2 + 2
        if yellow == (a-2) * (b-2):
            return [max(a,b), min(a,b)]