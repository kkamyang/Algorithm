# 2609

a, b = map(int, input().split())
i = a

while i <= a:
  if a % i == 0 and b % i == 0:
    break
  else:
    i -= 1

print(i, a*b//i, sep='\n')