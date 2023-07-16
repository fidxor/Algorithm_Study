from typing import Any, Type

class ListNode:
    '''연결 리스트용 노드 클래스'''
    def __init__(self, data : Any = None, next : Any = None):
        '''초기화'''
        self.data = data    # 데이터
        self.next = next    # 뒤쪽 포인터


class LinkedList:
    '''연결 리스트 클래스'''

    def __init__(self) -> None:
        '''초기화'''
        self.no = 0
        self.head = None
        self.current = None

    def __len__(self) -> int:
        '''연결 리스트의 노드 개수를 반환'''
        return self.no
    
    def search(self, data: Any) -> int:
        '''data와 값이 같은 노드를 검색'''
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.currentn = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data: Any) -> bool:
        '''연결 리스트에 data가 포함되어 있는지 확인'''
        return self.search(data) >= 0
    
    def add_first(self, data: Any) -> None:
        '''맨앞에 노드를 삽입'''
        ptr = self.head # 삽입하기전의 머리노드
        self.head = self.current = ListNode(data, ptr)
        self.no += 1

    def add_last(self, data: Any):
        ''' 맨 끝에 노드를 삽입'''
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = ListNode(data, None)
            self.no += 1

    def remove_first(self) -> None:
        '''머리노드를 삭제'''
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self):
        '''꼬리 노드를 삭제'''
        if self.head is not None:       # 노드가 비어있지 않다면
            if self.head.next is None:  # 노드가 1개 뿐이라면
                self.remove_first()     # 머리 노드를 삭제
            else:
                ptr = self.head         # 스캔중인 노드
                pre = self.head         # 스캔중인 노드의 앞쪽 노드

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None         # pre는 삭제 뒤 꼬리 노드
                self.current = pre
                self.no -= 1

    def remove(self, p: ListNode) -> None:
        '''노드 p를 삭제'''
        if self.head is not None:       # 노드가 비어있지 않으면
            if p is self.head:          # p가 머리 노드이면
                self.remove_first()     # 머리노드를 삭제
            else:
                ptr = self.head

                while ptr.next is not p:    # ptr 다음 노드가 p이면 while문 탈출
                    ptr = ptr.next
                    if ptr is None:
                        return          # ptr은 리스트에 존재하지 않음
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_cutrrent_node(self) -> None:
        '''주목노드를 삭제'''
        self.remove(self.current)

    def clear(self) -> None:
        '''전체노드를 삭제'''
        while self.head is not None:        # 전체가 비어있을 때까지
            self.remove_first()             # 머리노드를 삭제
        self.current = None
        self.no = 0

    def next(self) -> bool:
        '''주목 노드를 한칸 뒤로 이동'''
        if self.current is None or self.current.next is None:
            return False        # 이동할 수 없음
        self.current = self.current.next
        return True
    
    def print_current_node(self) -> None:
        '''주목 노드를 출력'''
        if self.current is None:
            print("주목 노드가 존재하지 않습니다.")
        else:
            print(self.current.data)

    def print(self) -> None:
        '''모든 노드를 출력'''
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def __iter__(self):
        '''이터레이터를 반환'''
        return LinkedListIterator(self.head)

class LinkedListIterator:
    '''클래스 LinkedList의 이터레이터용 클래스'''

    def __init__(self, head: ListNode):
        self.current = head

    def __iter__(self):
        return self
    
    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data



        
    

