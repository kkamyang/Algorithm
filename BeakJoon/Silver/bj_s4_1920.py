# 1920
import sys
import time

start = time.process_time()

N = int(sys.stdin.readline())
A = [int(x) for x in sys.stdin.readline().split()]
M = int(sys.stdin.readline())
B = [int(x) for x in sys.stdin.readline().split()]

for m in B:
  if m in A:
    print(1)
  else:
    print(0)
    
end = time.process_time()
print(end-start)