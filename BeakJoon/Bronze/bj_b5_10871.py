# 10871

N, X = map(int, input().split())
l = list(map(int, input().split()))
m = []

for i in l:
  if i < X:
    m.append(i)

for j in range(len(m)):
  print(m[j], end=' ')