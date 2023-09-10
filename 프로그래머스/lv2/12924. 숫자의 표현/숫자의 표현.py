def solution(n):
    ans = 0
    for i in range(1,n+1):
        
        cum_sum = i
        point = i
        while cum_sum < n:
            point += 1
            cum_sum += point
        if cum_sum == n:
            ans += 1
            
    return ans
            
            