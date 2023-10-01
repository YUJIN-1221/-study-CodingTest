def solution(k, dungeons):
    
    counts_list = []
    minimum = [i[0] for i in dungeons]
    used = [i[1] for i in dungeons]
    def recur(c_k=k, c_minimum=minimum, c_used=used, counts=0):
        if c_minimum == []:
            counts_list.append(counts)
        elif c_k < min(c_minimum):
            counts_list.append(counts)
        else:
            for i in range(len(c_minimum)):
                if c_k >= c_minimum[i]:
                    temp_minimum = c_minimum[:]
                    temp_used = c_used[:]
                    temp_minimum.pop(i)
                    temp_used.pop(i)
                    recur(c_k-c_used[i], temp_minimum, temp_used, counts+1)
                    
    recur(c_k=k, c_minimum=minimum, c_used=used, counts=0)
    
    return max(counts_list)