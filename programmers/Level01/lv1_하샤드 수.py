def solution(x):
    answer = False
    if x <= 10:
        answer = True
    elif x < 100:
        a = x%10
        b = x//10
        if x%(a+b)==0:
            answer = True
    elif x < 1000:
        a = x%10
        b = (x//10)%10
        c = x//100
        if x%(a+b+c)==0:
            answer = True
    elif x < 10000:
        a = x%10
        b = (x//10)%10
        c = (x//100)%10
        d = x//1000
        if x%(a+b+c+d)==0:
            answer = True
    elif x == 10000:
        answer = True
    return answer