import sys
def binarySearch(array, target, left, right): 
    while left<=right:
        mid = (left+right)//2 
        middle = array[mid]
        if target == middle:
            return 1
        elif middle > target:
            right=mid-1
        elif middle < target:
            left=mid+1
    return 0
  
n=int(sys.stdin.readline())
a=sorted(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))

for i in range(m):
    print(binarySearch(a, b[i], 0, n-1))