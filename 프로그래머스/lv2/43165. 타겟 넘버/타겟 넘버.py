def solution(numbers, target):
    
    def dfs(num_list, target):
        if len(num_list) == 0:
            if target == 0:
                return True
            else:
                return False
        
        num_f = num_list[0]
        
        return dfs(num_list[1:], target + num_f) + dfs(num_list[1:], target - num_f)
    
    return dfs(numbers, target)