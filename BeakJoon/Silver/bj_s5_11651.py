import sys
N = int(sys.stdin.readline())
l = []

for _ in range(N):
  n = list(map(int,sys.stdin.readline().split()))
  l.append(n)

l.sort(key=lambda x: (x[1], x[0]))

for i in l:
  print(i[0], i[1])