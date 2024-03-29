import sys
n, m, l = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.append(l)
a.sort()

left, right = 0, l-1
answer = 0

while left<=right:
    mid = (left+right)//2
    current, cnt = 0, 0

    for i in a:
        diff = i - current
        current = i
        if diff > mid: # 최대 거리보다 크므로 지어야함
            cnt += (diff-1)//mid
    if cnt > m: # m보다 많이 지음. 너무 가까이 지음
        left = mid+1
    else: # m보다 작거나 같게 지음. 너무 멀리 지음
        right = mid-1
        answer = mid 
print(answer)