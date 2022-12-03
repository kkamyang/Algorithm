def solution(arr):
    if len(arr)==1:
        answer = [-1]
    else:
        min = arr[0]
        for i in arr:
            if i<min:
                min = i
        arr.remove(min)
        answer = arr
    return answer