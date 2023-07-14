from linkedList import *

def addTwoNumbers(l1, l2):
    lst1, p1 = [], l1
    lst2, p2 = [], l2

    while p1 is not None:
        lst1.append(p1.data)
        p1 = p1.next

    while p2 is not None:
        lst2.append(p2.data)
        p2 = p2.next

    lst1 = lst1[::-1]
    lst2 = lst2[::-1]

    lstNum1 = ''.join(map(str, lst1))
    lstNum2 = ''.join(map(str, lst2))

    num1 = int(lstNum1)
    num2 = int(lstNum2)

    num3 = num1 + num2

    lst3 = list([int(a) for a in str(num3)])

    head = Node(lst3[0])    
    for i in range(1, len(lst3)):
        ptr = head
        head = Node(lst3[i], ptr)


    return head
        

    
        

list1 = LinkedList()
list2 = LinkedList()

list1.add_first(3)
list1.add_first(4)
list1.add_first(2)

list2.add_first(4)
list2.add_first(6)
list2.add_first(5)

addTwoNumbers(list1.head, list2.head)