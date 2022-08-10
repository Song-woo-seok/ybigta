from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1)

for i in range(m):
    a = list(map(int, input().split()))
    for j in range(1, a[0]):
        graph[a[j]].append(a[j+1])
        indegree[a[j+1]] += 1
print(a)
print(graph)
print(indegree)