n=int(input())
p=list(map(int,input().split()))
p.sort()
ans=0
answer=0
for i in p:
    ans+=i
    answer+=ans
print(answer)