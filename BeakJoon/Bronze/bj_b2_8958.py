# 8958

N = int(input())

for _ in range(N):
  aa = list(input())
  score = []  
  for i in range(len(aa)):
    if aa[i] == 'O':
      if i == 0:
        score.append(1)
      elif aa[i-1] == 'O':
        score.append(score[i-1]+1)
      else:
        score.append(1)
    else:
      score.append(0)
  print(sum(score))