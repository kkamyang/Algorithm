# 10773

a = []

for i in range(int(input())):
  num = int(input())
  if num != 0:
    a.append(num)
  elif (num == 0) & (len(a) != 0):
    a.pop()

print(sum(a))