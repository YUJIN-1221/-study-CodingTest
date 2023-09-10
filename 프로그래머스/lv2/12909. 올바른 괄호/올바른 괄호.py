def solution(s):
    c = 0
    
    for i in s:
        if c < 0:
            return False
        if i == '(':
            c += 1
        else:
            c -= 1
    if c == 0:
        return True
    else:
        return False