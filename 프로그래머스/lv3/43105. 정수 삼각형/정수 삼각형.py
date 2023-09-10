def solution(triangle):
    cusum_list = []
    
    for row in range(len(triangle)):
        temp = []
        
        if row == 0:
            temp.append(triangle[row][0])
            
        else:
            for idx in range(len(triangle[row])):
                if idx == 0:
                    temp.append(triangle[row][0]+cusum_list[row-1][0])
                elif idx == len(triangle[row])-1:
                    temp.append(triangle[row][-1]+cusum_list[row-1][-1])
                else:
                    temp.append(
                        max(triangle[row][idx]+cusum_list[row-1][idx-1], triangle[row][idx]+cusum_list[row-1][idx])
                           )
            
        cusum_list.append(temp)
        
    return max(cusum_list[-1])
        
#     sum_list = []
    
#     def dfs(row = 0, point = 0, cusum = 0):
#         if row == len(triangle)-1:
#             sum_list.append(cusum + triangle[row][point])
#         else: 
#             cusum += triangle[row][point]
#             dfs(row+1, point, cusum)
#             dfs(row+1, point+1, cusum)
        
#     dfs(row = 0, point = 0, cusum = 0)
    
#     return max(sum_list)