import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

a.sort()

dp = [1]*n
for i in range(n):
    for j in range(i):
        if a[i][1] > a[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(n-max(dp))