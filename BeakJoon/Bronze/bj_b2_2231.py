# 2231

n = int(input())

for i in range (n):
    m = 0
    n1 = i%10
    n2 = (i%100)//10
    n3 = (i%1000)//100
    n4 = (i%10000)//1000
    n5 = (i%100000)//10000
    n6 = (i%1000000)//100000
    if (i+n1+n2+n3+n4+n5+n6)==n:
        m = i 
        break
      
print(m)