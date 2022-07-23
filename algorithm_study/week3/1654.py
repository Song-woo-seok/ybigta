import sys
k, n = map(int, input().split())
a = [int(sys.stdin.readline()) for i in range(k)]
start, end = 1, max(a)

while start <= end:
    mid = (start + end) // 2
    line = 0 
    for i in a:
        line += i // mid 
        
    if line >= n: 
        start = mid + 1
    else:
        end = mid - 1
print(end)