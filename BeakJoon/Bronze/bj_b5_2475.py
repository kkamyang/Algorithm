# 2475

def sqr(x):
      return x**2

a, b, c, d, e = map(int, input().split())
num = (sqr(a) + sqr(b) + sqr(c) + sqr(d) + sqr(e)) % 10

print(num)