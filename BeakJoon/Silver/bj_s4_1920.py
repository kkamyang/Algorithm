# 1920
N = int(input())
dataAry = list(map(int, input().split()))
dataAry = sorted(dataAry)

M = int(input())
findAry = list(map(int, input().split()))

def binSearch(ary, fData):
  pos = -1
  start = 0
  end = len(ary) -1

  while (start <= end):
    mid = (start + end) // 2
    if fData == ary[mid]:
      return mid
    elif fData > ary[mid]:
      start = mid +1
    else:
      end = mid -1

  return pos

for i in findAry:
  position = binSearch(dataAry, i)
  if position == -1:
    print(0)
  else:
    print(1)