# 2292

n = int(input())
i = 1
count = 1

while i < n:
  i += 6*count
  count += 1

print(count)