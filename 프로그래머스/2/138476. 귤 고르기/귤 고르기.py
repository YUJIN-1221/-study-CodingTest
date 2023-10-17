def solution(k, tangerine):
    t_dict = {}
    for t in tangerine:
        if t in t_dict.keys():
            t_dict[t] = t_dict[t] + 1
        else:
            t_dict[t] = 1
            
    t_values = sorted(list(t_dict.values()), reverse=True)
    idx = 0
    while True:
        if k == 0:
            return idx
        elif k < t_values[0]:
            idx += 1
            return idx
        else:
            k -= t_values.pop(0)
            idx += 1