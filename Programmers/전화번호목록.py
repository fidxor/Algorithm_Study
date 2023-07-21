def solution(phone_book):
    answer = True
    phonedict = {}

    

    return answer


print(solution(["12","4875", "9901", "123","1235","567", "777", "88"]))
# print(solution(['123', '456', '789']))
# print(solution(["119", "97674223", "1195524421"]))

	

'''
시간 초과
일단 한번
def solution(phone_book):
    answer = True

    phone_book = sorted(phone_book, key=lambda x : len(x))    

    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False

    return answer

def solution(phone_book):
    answer = True
    count = 0

    phone_book = sorted(phone_book, key=lambda x : len(x))    

    for i in range(len(phone_book)):
        count = 0
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
            if j != len(phone_book) - 1:
                if phone_book[i] == phone_book[len(phone_book) - 1 - count][:len(phone_book[i])]:
                    return False
                
                count += 1
                if j + i == count:
                    break

    return answer
'''