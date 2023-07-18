def solution(a, b):
    answer = 0
    temp_list = []
    if a > b:
        temp_list = list(range(a, b - 1, -1))
    elif a < b:
        temp_list = list(range(a, b  + 1))
    else:
        temp_list = [a]

    for i in temp_list:
        answer += i
    return answer

