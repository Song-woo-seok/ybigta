length, width, height = map(int, input().split())
n = int(input())
lst = [list(map(int, input().split())) for i in range(n)]

volume = length * width * height
ans = 0
before = 0
lst.sort(reverse=True)

for i, j in lst:
    before *= 8
    v = 2 ** i
    
    maxc = (length // v) * (width // v) * (height // v) - before
    maxc = min(j, maxc)
    ans += maxc
    before += maxc

if before == volume:
    print(ans)
else:
    print(-1)