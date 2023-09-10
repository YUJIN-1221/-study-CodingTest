def solution(n):
    n_2 = 0; n_1 = 1
    
    for i in range(n-1):
        new_n = n_2 + n_1
        n_2 = n_1
        n_1 = new_n    
        
    return new_n % 1234567