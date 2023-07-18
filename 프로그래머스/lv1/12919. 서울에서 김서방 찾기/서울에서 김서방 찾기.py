def solution(seoul):
    answer = ''
    tempList = []
    for name in seoul:
        tempList.append(name.lower())
    
    index = tempList.index("kim")

    answer = "김서방은 {0}에 있다".format(index)
    return answer