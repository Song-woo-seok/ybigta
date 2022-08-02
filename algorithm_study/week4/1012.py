import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n): 
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1  
                dfs(nx, ny)
           
t = int(input())
for i in range(t):
    count = 0
    m, n, k = map(int, input().split())
    graph = [[0]*m for i in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for x in range(m):
        for y in range(n): 
            if graph[y][x] == 1:
                dfs(x, y)
                count += 1
    print(count)