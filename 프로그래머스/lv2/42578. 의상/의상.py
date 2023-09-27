import itertools

def solution(clothes):
    # list of [value, key]
    clothes_dict = {}
    for element in clothes:
        if element[1] in clothes_dict.keys():
            clothes_dict[element[1]].append(element[0])
        else:
            clothes_dict[element[1]] = [element[0]]
            
    num_list = [len(clothes_dict[key]) for key in clothes_dict.keys()]
    
    # ans = 0
    # for n in range(1, len(clothes_dict.keys())+1):
    #     for combi in list(map(list, itertools.combinations(num_list, n))):
    #         temp = 1
    #         for i in combi:
    #             temp *= i
    #         ans += temp        
    ans = 1
    for n in num_list:
        ans *= (n+1)
    
    return ans-1