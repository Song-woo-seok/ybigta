def fibonacci(n):
    f=[[0]*2 for i in range(41)]
    f[0]=[1,0]
    f[1]=[0,1]
    
    for j in range(2,n+1):
        f[j][0] = f[j - 1][0] + f[j - 2][0]
        f[j][1] = f[j - 1][1] + f[j - 2][1]
    return f[n]
import sys
t=int(sys.stdin.readline())
for k in range(t):
    n=int(sys.stdin.readline())
    print(fibonacci(n)[0],fibonacci(n)[1])