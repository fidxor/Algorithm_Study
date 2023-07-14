'''
가장 큰 수
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

'''
def solution(numbers: int) -> int:
    answer = ''

    # 숫자로 크기를 비교하는게 아니고 스트링으로 크기를 비교한다.
    numbers = list(str(x) for x in numbers)    
    lst = sorted(numbers, key=lambda x:x * 3, reverse=True)

    print(lst)

    answer = ''.join(lst)

    return str(int(answer))

print(solution([9, 98, 999, 998, 99, 8, 898]))
# [3, 30, 34, 5, 9]	"9534330"



'''
시간초과
def solution(numbers):
    answer = ''
        
    numbers = list(permutations(numbers, len(numbers)))
    lst = []

    for i in numbers:
        strnum = ''.join(map(str, i))
        lst.append(int(strnum))

    answer = str(max(lst))

    return answer

def solution(numbers):
    answer = ''

    # numbers = list(permutations(numbers, len(numbers)))
    numbers = list(map(''.join, permutations(map(str, numbers), len(numbers))))
    
    answer = max(numbers)

    return answer

테스트케이스 11 실패
def solution(numbers):
    answer = ''

    numbers = list(str(x) for x in numbers)    

    # 숫자로 크기를 비교하는게 아니고 스트링으로 크기를 비교한다.
    lst = sorted(numbers, key=lambda x:x * 3, reverse=True)

    answer = ''.join(lst)

    return answer

print(solution([3, 30, 34, 5, 9]))
'''

def solution_1(lst):
    answer = ''
    tmplst = []

    numbers = list(str(x) * 2 for x in lst)    

    numbers.sort(reverse=True)

    print(numbers)

    for i in numbers:
        tmplst.append(i[:len(i) // 2])

    print(tmplst)

    return answer

print(solution_1([9, 98, 999, 998, 99, 8, 898]))
# print(solution_1([3, 303, 34, 5, 9, 515, 30]))


print("3" < "30")