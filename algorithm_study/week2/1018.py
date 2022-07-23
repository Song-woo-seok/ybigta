n, m = map(int, input().split())
ori = []
count = []

for i in range(n):
    ori.append(input())

for a in range(n-7):
    for b in range(m-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if ori[i][j] != 'W':
                        index1 += 1
                    if ori[i][j] != 'B':
                        index2 += 1
                else:
                    if ori[i][j] != 'B':
                        index1 += 1
                    if ori[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))