def solution(arr):
    answer = []

    # not in을 사용 했더니 뒤에 있는 같은 숫자까지 안나오게 됨
    # for i in arr:
    #     if i not in answer:
    #         answer.append(i)

    index = 0

    for i in arr:
        if not answer:  #리스트가 비어있으면 arr의 첫번째 값은 무조건 append
            answer.append(i)
        elif i != answer[index]:
            answer.append(i)
            index += 1
    
    return answer