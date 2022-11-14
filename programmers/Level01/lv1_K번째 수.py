def solution(array, commands):
    answer = []
    for num in commands:        
        i, j, k = num[0], num[1], num[2]
        list = sorted(array[i-1:j])
        answer.append(list[k-1])
    return answer