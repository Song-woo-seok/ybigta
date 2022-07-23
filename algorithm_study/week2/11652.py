import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
cards = [int(input()) for i in range(n)]

count = Counter(sorted(cards))
print(count.most_common(1)[0][0])