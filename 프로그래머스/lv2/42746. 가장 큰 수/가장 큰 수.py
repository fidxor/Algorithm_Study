def solution(numbers):
    answer = ''

    # 숫자로 크기를 비교하는게 아니고 스트링으로 크기를 비교한다.
    numbers = list(str(x) for x in numbers)    
    lst = sorted(numbers, key=lambda x:x * 3, reverse=True)

    answer = ''.join(lst)

    return str(int(answer))