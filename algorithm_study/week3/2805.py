import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
start, end = 1, max(a)

while start <= end:
    mid = (start + end) // 2
    tree = 0 
    for i in a:
        if i>mid:
            tree += i - mid 
        
    if tree >= m: 
        start = mid + 1
    elif tree < m:
        end = mid - 1
print(end)