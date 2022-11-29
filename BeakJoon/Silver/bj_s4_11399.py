import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P = sorted(P)
l = []
count = 0
result = 0

for i in P:
  count += i
  l.append(count)

for i in l:
  result += i

print(result)