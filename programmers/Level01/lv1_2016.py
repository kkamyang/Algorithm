from datetime import datetime

def solution(a, b):
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0
    
    while i < (a - 1):
        b += month[i]
        i += 1
    
    return day[b % 7]