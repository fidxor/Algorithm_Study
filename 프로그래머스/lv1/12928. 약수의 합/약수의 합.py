def solution(n):
    answer = 0

    tempList = []

    for i in range(1, n + 1):
        if n % i == 0:
            tempList.append(i)

    for i in tempList:
        answer += i

    return answer

result = solution(12)
print(result)