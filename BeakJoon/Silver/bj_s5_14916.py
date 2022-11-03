n = int(input())
count = 0

if (n == 1) or (n == 3):
  count = -1
elif n%5 == 0:
  count += n//5
  n = n%5
else:
  while n%5 != 0:
    n -= 2
    count += 1
  count += n//5

print(count)