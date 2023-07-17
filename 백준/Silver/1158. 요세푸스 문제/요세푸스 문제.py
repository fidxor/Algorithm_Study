from collections import deque

N, K = map(int, input().split())

numbersLst = deque(range(1, N + 1))
resultLst = []

count = 0

while len(numbersLst) > 0:
    if count == K - 1:
        resultLst.append(numbersLst.popleft())
        count = 0
    else:
        numbersLst.append(numbersLst.popleft())
        count += 1

    # resultLst = "<" + ", ".join(str(x) for x in resultLst) + ">"
resultLst = str(resultLst).replace('[', '<').replace(']', '>')

print(resultLst)