def solution(numbers):
    
    def check(num, idx = 2): 
        if idx == int(num**0.5)+1:  # 소수일 때
            return True
        elif num % idx == 0:  # 소수가 아닐 때
            return False
        else:
            return check(num, idx+1)
        
    def permutation(nums, n):
        result = []
        
        if n == 1:
            for i in nums:
                result.append([i])  
                
        elif n > 1:
            for i in range(len(nums)):
                ans = [n for n in nums]
                ans.pop(i)
                for p in permutation(ans, n-1):
                    result.append([nums[i]]+p)
        return result
    
    
    answer = 0
    checked = []
    for l in range(1, len(numbers)+1):
        for i in permutation(list(numbers), l) :
            num = int(''.join(i))
            if num == 1:
                pass
            elif num in checked:
                pass
            else:
                answer += check(num)
                checked.append(num)
            
    return answer