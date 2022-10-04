# 2738

import sys

N, M = map(int, sys.stdin.readline().split())
a = []
b = []

for _ in range(N):
  a.append(list(map(int, sys.stdin.readline().split())))
for _ in range(N):
  b.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
  for j in range(M):
    print(a[i][j]+b[i][j], end=' ')
  print()