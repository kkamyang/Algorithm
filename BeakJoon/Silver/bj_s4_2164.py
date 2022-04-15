# 2164

from collections import deque

N = int(input())
card = deque(range(1, N+1))

while N != 1:
  del card[0]           
  card.rotate(-1) 
  N -= 1

print(card[0])