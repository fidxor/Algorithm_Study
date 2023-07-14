# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 각각의 헤드 노드와 빈 리스트를 새로 만들어 준다.
        lst1, p1 = [], l1
        lst2, p2 = [], l2

        # linkedlist를 돌면서 각 노드의 val값을 리스트에 넣어준다.
        while p1 is not None:
            lst1.append(p1.val)
            p1 = p1.next

        while p2 is not None:
            lst2.append(p2.val)
            p2 = p2.next

        # 리스트를 역순으로 변경한다.
        lst1 = lst1[::-1]
        lst2 = lst2[::-1]

        lstNum1 = ''.join(map(str, lst1))
        lstNum2 = ''.join(map(str, lst2))

        num1 = int(lstNum1)
        num2 = int(lstNum2)

        # 역순으로 변경한 리스트들을 각각 정수형으로 변환하고 더해준다
        num3 = num1 + num2

        # 더한 값을 다시 리스트로 만들어 준다.
        # 여기서 생성한 리스트는 정답리스트의 역순이다.
        lst3 = list([int(a) for a in str(num3)])

        '''
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

        위에 테스트 케이스를 기준으로

        lst3 = [8, 0, 7]
        1. ListNode에 8의 값을 넣어주고 head를 생성해 준다 여기에 생성된 ListNode에 다음을 가르키는 next가 none이다.
            그다음 반복문에서 ptr 임시 변수에 head를 넣어주고
        2. ListNode에 0의 값을 넣어주고 next에 head를 넣어둔 ptr을 넣어주고 head를 지금 생성한 ListNode로 변경한다.
             그렇게 되면 0의 값을 가지고 있는 노드가 head가 되고 가르키고 있는 노드는 8의 값을 가지고 있는 노드가 된다.
        3. 마지막으로 2번에서 진행된것과 똑같이 7의 값을 넣어주고 0의값을 가진 노드를 가르키도록 next에 0의 값을 가진 노드를 넣어준다.

        이렇게 LinkedList를 생성해 주면

        7의 값을 가지고 있는 노드가 head가 되서 맨앞에 위치하게 되고 그다음 순서대로 0 -> 8 의 값을 가지게 되는 linkedlist가 만들어진다
        7 -> 0 -> 8
        '''
        head = ListNode(lst3[0])    
        for i in range(1, len(lst3)):
            ptr = head
            head = ListNode(lst3[i], ptr)

        return head
        


