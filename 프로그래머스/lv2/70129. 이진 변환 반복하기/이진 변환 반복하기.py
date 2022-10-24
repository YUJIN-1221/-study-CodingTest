def solution(s):
    
    def dfs(s_trans, num_trans, num_0):
        if s_trans == '1':
            return [num_trans, num_0]
        
        num_0 += s_trans.count('0')
        s_trans = s_trans.replace('0', '', s_trans.count('0'))
        s_trans =  str(bin(len(s_trans))[2:])
        num_trans += 1
        return dfs(s_trans, num_trans, num_0)
    
    return dfs(s, 0, 0)