from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for i in range(n)] for j in range(h)]

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if -1<nx<n and -1<ny<m and -1<nz<h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y]+1
                    q.append((nz,nx,ny))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i,j,k))

