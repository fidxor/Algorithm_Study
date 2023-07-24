def solution(phone_book):
    answer = True
    phonedict = {}
    index = 0
    
    # phone_book 리스트의 값들을 key값으로 dict를 만든다 
    for i in phone_book:
        phonedict[i] = index
        index += 1

    # 각 문자열의 앞자리부터 비교해서 key값을 찾아서 있으면 False
    for i in phonedict:
        key = ""
        for j in i:
            key += j
            if key != i:
                if key in phonedict:
                    return False

    return answer