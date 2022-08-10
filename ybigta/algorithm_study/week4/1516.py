from math import degrees
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

build = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    graph = list(map(int, input().split()))
    time[i] = graph[0]

    for j in range(1, len(graph)-1):
        build[graph[j]].append(i)
        indegree[i] += 1

dp = [0]*(n+1)
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] += time[i]

while q:
    a = q.popleft()
    for i in build[a]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[a] + time[i])
        if indegree[i] == 0:
            q.append(i)
print(*dp[1:], sep="\n")