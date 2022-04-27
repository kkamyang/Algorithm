# 2407

n, k = map(int, input().split())
K, N = 1, 1

for i in range(k):
  K *= i+1
  N *= n-i
print(N//K)