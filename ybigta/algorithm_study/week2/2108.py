import sys
from collections import Counter
n=int(sys.stdin.readline())
b=[]
for i in range(n):
    a=int(sys.stdin.readline())
    b.append(a)
    
print(round(sum(b)/n))
b.sort()
c=b[:]
print(b[n//2])

b=Counter(b).most_common()

if len(b) > 1:
    if b[0][1] == b[1][1]:
        print(b[1][0])
    else:
        print(b[0][0])
else:
    print(b[0][0])
    
print(c[n-1]-c[0])