def solution(bridge_length, weight, truck_weights):
    current = [0 for i in range(bridge_length)]
    # weight --> 가능한 최대 무게, bridge_length --> 걸리는 시간  & 가능한 최대 트럭 수
    
    time = 0
    weight_now = 0
    while True:
        if truck_weights:  # 출발하지 않은 트럭 있음 
            time += 1
            weight_now -= current.pop(0)            
            if weight_now + truck_weights[0] <= weight:
                c = truck_weights.pop(0)
                weight_now += c
                current.append(c)
            else:
                current.append(0)
        else:  # 모든 트럭이 다 출발함
            if weight_now == 0:
                break
            else:
                time += 1
                weight_now -= current.pop(0)
                current.append(0)
        
    return time

# def solution(bridge_length, weight, truck_weights):
#     current = [0 for i in range(bridge_length)]
#     # weight --> 가능한 최대 무게, bridge_length --> 걸리는 시간  & 가능한 최대 트럭 수
    
#     time = 0
#     while True:
#         if truck_weights:  # 출발하지 않은 트럭 있음 
#             time += 1
#             current.pop(0)
#             if sum(current) + truck_weights[0] <= weight:
#                 c = truck_weights.pop(0)
#                 current.append(c)
#             else:
#                 current.append(0)
#         else:  # 모든 트럭이 다 출발함
#             if sum(current) == 0:
#                 break
#             else:
#                 time += 1
#                 current.pop(0)
#                 current.append(0)
        
#     return time