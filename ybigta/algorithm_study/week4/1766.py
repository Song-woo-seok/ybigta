import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())

answer = []
graph = [[] for i in range(n+1)]
indegree = [0 for i in range(n+1)]
queue = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)
    for i in graph[tmp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(queue, i)

print(" ".join(map(str, answer)))