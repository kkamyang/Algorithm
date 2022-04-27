# 11050
n, k = map(int, input().split())
K, N = 1, 1

if k == 0:
  print(1)
else:
  for i in range(k):
    K *= i+1
    N *= n-i
  print(N//K)