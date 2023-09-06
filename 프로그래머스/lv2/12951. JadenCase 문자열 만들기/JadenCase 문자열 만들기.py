def solution(s):
    str_list = s.split(' ')
    changed_list = []
    for w in str_list:
        if len(w) == 0:
            changed_list.append(w)
        elif w[0].isnumeric():
            changed_list.append(w.lower())
        else:
            changed_list.append(w[0].upper()+w[1:].lower())
    
    return ' '.join(changed_list)  