def solution(s):
    a = list(s)
    a.sort(), a.reverse()
    return ("".join(a))