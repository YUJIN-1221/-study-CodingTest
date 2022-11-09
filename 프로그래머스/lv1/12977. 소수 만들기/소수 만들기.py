import itertools

def solution(nums):

    def check(num, idx = 2):  # nums는 최소 1+2+3=6
        if idx == int(num**0.5)+1:  # 소수일 때
            return True
        elif num % idx == 0:  # 소수가 아닐 때
            return False
        else:
            return check(num, idx+1)
        
#     def combination(nums, n):
#         result = []
        
#         if n == 1:
#             for i in nums:
#                 result.append([i])
                
#         elif n > 1:  # n이 3이라면
#             for i in range(len(nums)-n+1):  # 0,...,len(nums)-3
#                 for j in combination(nums[i+1:], n-1):  # i 이후 리스트의 2 조합 리스트
#                     result.append([nums[i]]+j)
                    
#         return result
    
    ans = 0
    for l in itertools.combinations(nums, 3):
        ans += check(sum(l))

    return ans