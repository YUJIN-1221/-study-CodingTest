def solution(s):
    c_dict = {'(':')', '[':']', '{':'}'}
    
    def check(sub_s):
        sub_s = list(sub_s)
        stack = []
        while sub_s:
            c = sub_s.pop(0)
            if c in c_dict.keys():
                stack.append(c_dict[c])
            else:
                if stack:
                    if c == stack[-1]:
                        stack.pop(-1)
                    else:
                        return 0
                else:
                    return 0
        if stack:
            return 0
        else:
            return 1
    
    ans = 0
    for i in range(len(s)):
        ans += check(s[i:] + s[:i])
        
    return ans 