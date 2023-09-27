def solution(people, limit):
    if len(people) == 1:
         return 1
        
    people = sorted(people)
    
    l_idx = 0
    r_idx = len(people) - 1
    ans = 0
    
    while l_idx <= r_idx:
        
        if people[l_idx] + people[r_idx] <= limit:
            ans += 1
            l_idx += 1
            r_idx -= 1
        else:
            ans += 1
            r_idx -= 1
            
    return ans
    

# def solution(people, limit):
#     people = sorted(people)
    
#     if len(people) == 1:
#         return 1
    
#     ans = 0
    
#     while len(people) > 1:
#         if people[-1] + people[0] <= limit:
#             ans += 1
#             people.pop(-1); people.pop(0)
#         else:
#             ans += 1
#             people.pop(-1)
            
#     if people:
#         ans += 1
#         people.pop()
            
#     return ans