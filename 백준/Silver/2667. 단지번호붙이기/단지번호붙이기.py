n = int(input())

lad = []
for i in range(n):
    lad.append(list(map(int, input())))
    
def func(c,r):
    global count
    
    if c < 0 or c >= n or r < 0 or r >= n:
        pass
    else: 
        if lad[c][r] == 1:
            count += 1
            lad[c][r] = 0
            for i in range(4):
                func(c+dc[i], r+dr[i])
    return count    
    
part = 0
parts = {}
dc = [0, 0, 1, -1]
dr = [1, -1, 0, 0]

x, y = 0, 0
while x<n:
    if lad[x][y] == 0:
        if y == n-1:
            x+=1
            y=0
        else:
            y+=1
    else:
        part += 1
        count = 0
        parts[part] = func(x, y)
        
print(len(parts.keys()))
for i in sorted(parts.values()):
    print(i)