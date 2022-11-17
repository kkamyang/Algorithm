# 2108
import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
l = []

for i in range(N):
  n = int(sys.stdin.readline().rstrip())
  l.append(n)

# 산술평균
def mean(list):
  count = 0
  for i in list:
    count += i
  print(round(count/len(list)))

# 중앙값
def mid(list):
  list = sorted(list)
  i = len(list)//2
  print(list[i])
  
# 최빈값
def mode(list):
    c = Counter(list)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    if len(modes)==1:
      print(modes[0])
    else:
      modes = sorted(modes)
      print(modes[1])
      
# 범위
def ran(list):
  print(max(list) - min(list))

mean(l)
mid(l)
mode(l)
ran(l)