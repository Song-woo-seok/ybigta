import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cakes = list(map(int, input().split()))
cakes.sort(key=lambda x: (x%10,x))

ans = 0
for i in cakes:
    cnt = i//10
    if i%10==0:
        if cnt-1 <= m:
            ans += cnt
            m -= cnt -1
        else:
            ans += m
            m -= m
    else:
        if cnt <= m:
            ans += cnt
            m -= cnt
        else:
            ans += m
            m -= m
print(ans)