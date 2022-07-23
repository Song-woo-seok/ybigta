import sys
n, m, l = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
start, end = 1, max(a)

while start <= end:
    mid = (start + end) // 2
    station = 0 
    for i in a:
        if i>mid:
            station += i - mid 
        
    if station >= m: 
        start = mid + 1
    elif station < m:
        end = mid - 1
print(end)