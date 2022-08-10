n=1
while True:
    l,p,v=map(int, input().split())
    if l==0 and p==0 and v==0:
        break
    ans=(v//p)*l
    ans+=min((v%p),l)
    print('Case {}: {}'.format(n,ans))
    n+=1