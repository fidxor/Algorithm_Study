from __future__ import annotations
from typing import Any, Type

class Node:
    '''이진 검색 트리 노트'''
    def __init__(self, key: Any, value:Any, left:Node = None, right:Node = None):
        '''생성자'''
        self.key = key          # 키
        self.value = value      # 값
        self.left = left        # 왼쪽 노드 포인터
        self.right = right      # 오른쪽 노드 포인터

class BinarySearchTree:
    '''이진 검색 트리'''
    def __init__(self):
        '''초기화'''
        self.root = None        # 루트


    def search(self, key: Any):
        '''키가 key인 노드를 검색'''
        p = self.root           # root에 주목
        while True: 
            if p is None:       # 더 이상 진행할 수 없으면
                return None     # 검색 실패
            if key == p.key:    # key와 노드 p의 key와 같으면
                return p.value  # 검색 성공
            elif key < p.key:   # key 쪽이 작으면
                p = p.left      # 왼쪽 서브트리에서 검색
            elif key > p.key:   # key 쪽이 크면
                p = p.right     # 오른쪽 서브트리에서 검색

    def add(self, key: Any, value: Any):
        '''키가 key이고 값이 value인 노드를 삽입'''
        def add_node(node: Node, key: Any, value: Any):
            '''node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입'''
            if key == node.key:     # key가 이진 검색 트리에 이미 존재
                return False
            elif key < node.key:    # 추가 하려는 key가 노드key보다 작으면 
                if node.left is None:   # 노드의 left가 None 이면
                    node.left = Node(key, value, None, None)    # 추가 하려는 key 와 value 를 가진 노드를 부모노드 왼쪽 노드에 추가
                else:               # 왼쪽에 노드가 이미 존재 한다면
                    add_node(node.left, key, value)
            else:                   # 추가하려는 key가 노드key보다 크면
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else: 
                    add_node(node.right, key, value)

            return True
        
        if self.root is None:       # root가 없을 경우
            self.root = Node(key, value, None, None)        # 추가하려는 key와 value를 루트노드로 만들어 준다
            return True
        else:           # root 가 있을 경우
            return add_node(self.root, key, value)
        

    def remove(self, key: Any):
        '''키가 key인 노드를 삭제'''
        p = self.root           # p는 스캔중인 노드. root부터 시작한다.
        parent = None           # 스캔중인 노드의 부모노드
        is_left_child = True    # p는 parent의 왼쪽 자식 노드인지 확인.

        while True:
            if p is None:           # 더 이상 진행할 수 없으면
                return False        # 그 key는 존재하지 않음
            
            if key == p.key:        # key와 노드 p의 키가 같으면
                break               # 검색성공
            else:
                parent = p          # 가지를 내려가기전에 p를 부모 노드로 설정
                if key < p.key:     # key 쪽이 작으면
                    is_left_child = True    # 여기서 내려가는 것은 왼쪽 자식
                    p = p.left      # 왼쪽 서브트리를 검색
                else:               # key 쪽이 크면
                    is_left_child = False
                    p = p.right

        if p.left is None:          # p에 왼쪽 자식이 없으면
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right       # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right      # 부모의 오른쪽 포인처가 오른쪽 자식을 가리킴
        elif p.right is None:       # p에 오른쪽 사직이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left    # 부모의 왼쪽포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left       # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
        else:           # 왼쪽과 오른쪽 둘다 자식이 있으면
            parent = p
            left = p.left       # 서브트리 안에서 가장 큰 노드
            is_left_child = True
            while left.right is not None:   # 가장 큰 노드 left를 검색
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key            # left의 키를 p로 이동
            p.value = left.value        # left의 데이터를 p로 이동
            
            if is_left_child:               # left를 삭제
                parent.left = left.left
            else:
                parent.right = left.left
        return True
    
    def min_key(self):
        '''가장 작은 키'''
        if self.root is None:
            return None
        
        p = self.root
        while p.left is not None:
            p = p.left

        return p.key
    
    def max_key(self):
        '''가장 큰 키'''
        if self.root is None:
            return None
        
        p = self.root
        while p.right is not None:
            p = p.right

        return p.key
    
    def dump(self, reverse = False):
        '''모든 노드를 키의 오름차순/내리차순 으로 출력'''
        '''스캔은 중위 순회의 깊이 우선 검색으로 한다.'''

        def print_subtree(node: Node):
            '''node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력'''
            if node is not None:
                print_subtree(node.left)        # 왼쪽 서브트리를 오름차순으로 출력
                print("{0} {1}".format(node.key, node.value))   # node를 출력
                print_subtree(node.right)       # 오른쪽 서브트리를 오름차순으로 출력

        def print_subtree_rev(node: Node):
            '''node를 루트로 하는 서브트리의 노드를 키의 내림차순으로 출력'''
            if node is not None:
                print_subtree_rev(node.right)
                print("{0} {1}".format(node.key, node.value))
                print_subtree_rev(node.left)

        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

        

            