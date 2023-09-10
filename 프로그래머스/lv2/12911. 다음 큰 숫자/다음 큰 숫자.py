def solution(n):
    num_one = bin(n)[2:].count('1')
    
    while True:
        n += 1
        if bin(n)[2:].count('1') == num_one:
            break
            
    return n