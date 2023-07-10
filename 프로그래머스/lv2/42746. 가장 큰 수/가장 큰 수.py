def solution(numbers):
    answer = ''

    # 숫자로 크기를 비교하는게 아니고 스트링으로 크기를 비교한다.
    numbers = list(str(x) for x in numbers)    
    lst = sorted(numbers, key=lambda x:x * 3, reverse=True)

    answer = ''.join(lst)

    # 앞자리 수자 0일경우 0을 없애주기 위해 정수로 변경후 다시 문자열로 변환
    return str(int(answer))