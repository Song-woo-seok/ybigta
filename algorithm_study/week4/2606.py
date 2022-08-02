n = int(input())
m = int(input())
graph = [[]*n for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
count = 0
visited = [0]*(n+1)
def dfs(s):
    global count
    visited[s] = 1
    for i in graph[s]:
        if visited[i]==0:
            dfs(i)
            count +=1
dfs(1)
print(count)