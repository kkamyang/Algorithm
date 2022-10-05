# 10814

N = int(input())
l = []

for _ in range(N):
  age, name = input().split()
  l.append((int(age), name))

l = sorted(l, key=lambda x : x[0])

for i in range(N):
  print(l[i][0], l[i][1])