# 11650

N = int(input())
l = []

for i in range(N):
  xy = list(map(int, input().split()))
  l.append(xy)

l.sort()
for i in range(N):
  print(l[i][0], l[i][1], sep=' ')