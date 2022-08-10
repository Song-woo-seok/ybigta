def create(n):
    count=1
    while n//10>=1:
        count=count+1
        n=n//10
    return count

def check(n):
    a=[]
    sum=0
    real_n=n
    for i in range(create(n)):
        a.append(n%10)
        n=n//10
    for i in a:
        sum=sum+i
    return sum+real_n
        
n=int(input())
new=create(n)*9
num=n-new
c=0

for i in range(num, n):
    if i>0 and check(i)==n:
        break
    else:
        c=c+1

if c==new:
    print('0')
else:
    print(i)