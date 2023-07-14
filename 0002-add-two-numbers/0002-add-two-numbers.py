# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1, p1 = [], l1
        lst2, p2 = [], l2

        while p1 is not None:
            lst1.append(p1.val)
            p1 = p1.next

        while p2 is not None:
            lst2.append(p2.val)
            p2 = p2.next

        lst1 = lst1[::-1]
        lst2 = lst2[::-1]

        lstNum1 = ''.join(map(str, lst1))
        lstNum2 = ''.join(map(str, lst2))

        num1 = int(lstNum1)
        num2 = int(lstNum2)

        num3 = num1 + num2

        lst3 = list([int(a) for a in str(num3)])

        head = ListNode(lst3[0])    
        for i in range(1, len(lst3)):
            ptr = head
            head = ListNode(lst3[i], ptr)

        return head
        


