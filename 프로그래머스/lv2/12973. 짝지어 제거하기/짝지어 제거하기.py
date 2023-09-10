def solution(s):
    stack = []
    for i in range(len(s)):
        if stack == []:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop(-1)
            else:
                stack.append(s[i])
    return int(stack == [])