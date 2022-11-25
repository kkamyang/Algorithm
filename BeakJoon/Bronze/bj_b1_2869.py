# 2869
import sys

A, B, V = map(int,sys.stdin.readline().split())
N = (A-B)
M = (V-A)
if M%N == 0:
  count = 1 + M//N
else:
  count = 2 + M//N

print(count)