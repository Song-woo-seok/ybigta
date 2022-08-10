import sys
input = sys.stdin.readline

def check():
    for i in range(n-1):
        if arr[i + 1][0] - (arr[i][0] + arr[i][1]) >= m:
            return (arr[i][0] + arr[i][1])

arr = []
n, m, s = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))
arr.sort()

if arr[0][0] >= m:
    print(0)
elif check() != None:
    print(check())
elif arr[-1][0] + arr[-1][1] + m <= s:
    print(arr[-1][0] + arr[-1][1])
else:
    print(-1)