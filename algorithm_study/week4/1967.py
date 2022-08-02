import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for i in range(n + 1)]
ans = 0

for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dfs(x, d):
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = d + b
            dfs(a, d + b)

visited = [-1] * (n + 1) 
visited[1] = 0 
dfs(1, 0) 

start = visited.index(max(visited))

visited = [-1] * (n + 1) 
visited[start] = 0 
dfs(start, 0) 

print(max(visited))