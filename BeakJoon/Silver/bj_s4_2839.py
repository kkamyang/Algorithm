#2839
N = int(input())
count = 0

if (N == 4) or (N == 7):
  count = -1
elif N%5 == 0:
  count = N//5
  N = N%5
else:
  while N%5 != 0:
    N -= 3
    count += 1
  count += N//5

print(count)