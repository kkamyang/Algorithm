def solution(n, m):
    answer = []
    i = m
    
    while i < m+1:
        if n%i==0 and m%i==0:
            answer.append(i)
            break
        i -= 1
    answer.append(n*m/i)
    
    return answer