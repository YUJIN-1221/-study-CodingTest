def solution(A,B):
    A = sorted(A)
    B = sorted(B)
    
    if len(A) == 1:
        return A[0] * B[0]
    else:
        answer = 0
        for i in range(len(A)):
            answer += A[i] * B[-(i+1)]   
        return answer