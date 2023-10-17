def solution(n):
    import math
    
    ans = 0
    num_2 = 0
    num_1 = n
    while n > 0:
        ans += math.comb(n, num_2)
        n -= 1
        num_2 += 1
        num_1 -= 1
        
    return ans % 1234567