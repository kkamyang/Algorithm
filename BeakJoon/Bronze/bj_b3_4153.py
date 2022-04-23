#4153

while True:
  leg = list(map(int,input().split()))
  leg.sort()
  if sum(leg)==0:
    break
  elif leg[0]**2 + leg[1]**2 == leg[2]**2:
    print('right')
  else:
    print('wrong')