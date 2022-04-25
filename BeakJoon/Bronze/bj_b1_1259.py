# 1259

while True:
    a = list(map(int, str(input())))
    if a == [0]:
        break
    elif a == a[::-1]:
        print('yes')
    else:
        print('no')