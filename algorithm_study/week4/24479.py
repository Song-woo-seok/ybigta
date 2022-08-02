import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
link = [[] for i in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for i in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

for i in range(1,n+1):
    link[i].sort()

def dfs(v):
    global cnt
    visited[v] = cnt
    for i in link[v]:
        if visited[i]:
            continue
        cnt+=1
        dfs(i)
dfs(r)
print(*visited[1:], sep="\n")