import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
indegree = [0 for i in range(n+1)]
q = deque()
answer = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    tmp = q.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(*answer)