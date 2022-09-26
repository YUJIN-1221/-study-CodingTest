import heapq

n,m = list(map(int, input().split()))
problem = [[] for _ in range(n+1)]
prev_cnt = [0 for _ in range(n+1)]
q = []
answer = []

for _ in range(m):
    a, b=map(int, input().split())  # b -> a
    problem[a].append(b)
    prev_cnt[b]+=1
    
for i in range(1, n+1):
    if prev_cnt[i]==0:  # 먼저 풀 문제가 없는 문제 번호
        heapq.heappush(q, i)
        
while q:
    cur=heapq.heappop(q)
    answer.append(cur)
    for nxt in problem[cur]:
        prev_cnt[nxt]-=1
        if prev_cnt[nxt]==0:
            heapq.heappush(q, nxt)
            
print(*answer)