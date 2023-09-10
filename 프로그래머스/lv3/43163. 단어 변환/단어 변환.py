def solution(begin, target, words):
    if target not in words:
        return 0
    
    def check_(present, check_word):
        return sum([a!=b for a,b in zip(present, check_word)]) == 1
    
    ans_list = []
    def dfs(present = begin, target = target, words_renew = words, idx = 0):
        if present == target:
            ans_list.append(idx)
        
        for check_word in words_renew:
            if check_(present, check_word):
                temp = words_renew[:]
                temp.remove(check_word)
                dfs(check_word, target, temp, idx+1)                
                
    dfs(present = begin, target = target, words_renew = words, idx = 0)
    ans = min(ans_list) if ans_list else 0
    return ans