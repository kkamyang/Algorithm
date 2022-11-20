import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
result = 0

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(N):
  a = A[i] * B[i]
  result += a

print(result)