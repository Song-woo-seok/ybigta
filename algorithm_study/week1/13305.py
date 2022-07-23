import sys
input=sys.stdin.readline

n=int(input())
length=list(map(int,input().split()))
price=list(map(int,input().split()))
ans=0

c=price[0]
for i in range(n-1):
    if c>price[i]:
        c=price[i]
    ans+=c*length[i]
print(ans)