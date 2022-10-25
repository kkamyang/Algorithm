def solution(a, b):
    if b > a:
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))