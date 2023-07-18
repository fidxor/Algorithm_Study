def solution(x, n):
    answer = []    
    
    if(x > 0):
        answer = list(range(x, x * n + 1, x))
    elif(x < 0):
        answer = list(range(x, x * n - 1, x))
    else:
        answer = list([x] * n)

    return answer