from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False]*m for _ in range(n)]
    
    q = deque()
    q.append((0, 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[0][0]=True
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    maps[ny][nx] = maps[y][x]+1
    if maps[n-1][m-1]==1:
        return -1
    else:
        return maps[n-1][m-1]

# import copy

# def solution(maps):
#     n, m = len(maps)-1, len(maps[0])-1
    
#     idx_list = []
    
#     def dfs(current_position = [0, 0], current_maps = maps, idx = 1):
            
#         x, y = current_position[0], current_position[1]
#         if x == n and y == m:
#             idx_list.append(idx)
        
#         if x+1 <= n: # 남 
#             if current_maps[x+1][y] == 1:
#                 temp = copy.deepcopy(current_maps)
#                 temp[x+1][y] = 0
#                 dfs([x+1, y], temp, idx+1)
            
#         if x-1 >= 0:  # 북
#             if current_maps[x-1][y] == 1:
#                 temp = copy.deepcopy(current_maps)
#                 temp[x-1][y] = 0
#                 dfs([x-1, y], temp, idx+1)
            
#         if y+1 <= m:  # 동
#             if current_maps[x][y+1] == 1:
#                 temp = copy.deepcopy(current_maps)
#                 temp[x][y+1] = 0
#                 dfs([x, y+1], temp, idx+1)
            
#         if y-1 >= 0:  # 서
#             if current_maps[x][y-1] == 1:
#                 temp = copy.deepcopy(current_maps)
#                 temp[x][y-1] = 0
#                 dfs([x, y-1], temp, idx+1)
            
#     dfs(current_position = [0, 0], current_maps = maps, idx = 1)
    
#     return min(idx_list) if idx_list else -1