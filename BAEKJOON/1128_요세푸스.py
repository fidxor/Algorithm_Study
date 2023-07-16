'''
문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)
'''
from collections import deque

class ListNode:
    def __init__(self, data, next = None):
        self.data = data        
        self.next = next

N, K = map(int, input().split())
    
resultLst = deque()
count = 0
nodecnt = 0

#linkedList 생성
head = ListNode(1)
nodecnt += 1

ptr = head
for i in range(2, N + 1):
    temp = ListNode(i, head)
    ptr.next = temp
    ptr = ptr.next
    nodecnt += 1

while nodecnt > 0:
    if count == K - 1:
        # 노드 삭제
        resultLst.append(head.data)
        temp.next = head.next
        head = head.next

        nodecnt -= 1
        count = 0

    count += 1
    temp = head
    head = head.next
    

resultLst = str(resultLst).replace('[', '<').replace(']', '>')

resultLst



# <3, 6, 2, 7, 5, 1, 4>

'''
시간초과

N, K = map(int, input().split())

numbersLst = list(range(1, N + 1))
resultLst = []

count = 0
startIdx = 0

while len(numbersLst) > 0:
    if count == K - 1:
        resultLst.append(numbersLst.pop(startIdx))
        count = 0
        if(startIdx == len(numbersLst)):
            startIdx = 0

    count += 1
    startIdx += 1

    if startIdx > len(numbersLst) - 1:
        #startIdx가 numbersLst 맨끝에 도착하면 다시 앞으로 보낸다
        startIdx = 0

    # resultLst = "<" + ", ".join(str(x) for x in resultLst) + ">"
resultLst = str(resultLst).replace('[', '<').replace(']', '>')

print(resultLst)

시간초과

class ListNode:
    def __init__(self, data, next = None):
        self.data = data        
        self.next = next

N, K = map(int, input().split())
    
resultLst = []
count = 0
nodecnt = 0

#linkedList 생성
head = ListNode(1)
nodecnt += 1

ptr = head
for i in range(2, N + 1):
    temp = ListNode(i, head)
    ptr.next = temp
    ptr = ptr.next
    nodecnt += 1

while nodecnt > 0:
    if count == K - 1:
        # 노드 삭제
        resultLst.append(head.data)
        temp.next = head.next
        head = head.next

        nodecnt -= 1
        count = 0

    count += 1
    temp = head
    head = head.next
    

resultLst = str(resultLst).replace('[', '<').replace(']', '>')

print(resultLst)
'''