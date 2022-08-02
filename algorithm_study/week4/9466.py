import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = arr[x]
    
    if visited[number]: 
        if number in cycle:
            result += cycle[cycle.index(number):] 
    else:
        dfs(number)

t = int(input())
for i in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    result = []
    
    for i in range(1, n+1):
        if not visited[i]: 
            cycle = []
            dfs(i)
            
    print(n - len(result)) 