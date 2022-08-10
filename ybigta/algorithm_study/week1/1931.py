n=int(input())
ans=[]
for i in range(n):
    s,f=map(int,input().split())
    ans.append([s,f])
ans.sort()
ans=sorted(ans, key=lambda x: x[1])
last=0
count=0
for i,j in ans:
    if i>=last:
        count+=1
        last=j
print(count)