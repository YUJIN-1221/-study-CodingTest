def solution(participant, completion):
    completion_dict = {}
    for c in completion:
        if completion_dict.get(c) == None:
            completion_dict[c] = 1
        else:
            completion_dict[c] = completion_dict[c] + 1
            
    for p in participant:
        if completion_dict.get(p) == None:
            return p
        elif completion_dict.get(p) > 1:
            completion_dict[p] = completion_dict[p] - 1
        else:
            del completion_dict[p]