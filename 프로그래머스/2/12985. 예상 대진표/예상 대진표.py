def solution(n,a,b):
    ans = 1
    while True:
        if max(a,b) - min(a,b) == 1 and max(a,b) % 2 == 0:
            return ans
        a = (a+1) // 2
        b = (b+1) // 2
        ans += 1