# 최대 힙
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(None)

    # 해당 노드가 부모노드보다 큰지 비교
    def check_swap_up(self, idx):
        # 삽입한 노드의 부모 노드가 없을경우
        if idx <= 1:
            return False
        
        parent_idx = idx // 2

        if self.heap[idx] > self.heap[parent_idx]:
            return True
        else:
            return False

    # 데이터 삽입
    def insert(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1

        # check_swap_up() 의 값이 참이라면 부모와 자리 바꾸기
        while self.check_swap_up(idx):
            parent_idx = idx // 2

            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx

        return True
    
    # 해당 노드가 자식 노드보다 큰지 비교
    def check_swap_down(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        # 자식 노드가 하나도 없을 경우
        if left_idx >= len(self.heap):
            return False        
        # 왼쪽 자식노드만 있을 경우
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] > self.heap[idx]:
                self.flag = 1
                return True
            else:
                return False
        # 자식 노드가 모두 있을 경우        
        else:
            if self.heap[left_idx] > self.heap[right_idx]:
                if self.heap[left_idx] > self.heap[idx]:
                    self.flag = 1
                    return True
                else:
                    return False
            else:
                if self.heap[right_idx] > self.heap[idx]:
                    self.flag = 2
                    return True
                else:
                    return False
                
    # 데이터 삭제
    def pop(self):
        if len(self.heap) <= 1:
            return None
        
        max = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        idx = 1

        # 0 = False, 1 = 왼쪽자식과 swap, 2 = 오른쪽자식과 swap  
        self.flag = 0

        while self.check_swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1

            if self.flag == 1:
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx
            elif self.flag == 2:
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx
        
        return max

# 최소힙
class MinHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(None)

    def __len__(self):
        return len(self.heap)

    # 해당 노드가 부모노드보다 작은지 비교
    def check_swap_up(self, idx):
        # 삽입한 노드의 부모 노드가 없을경우
        if idx <= 1:
            return False
        
        parent_idx = idx // 2

        if self.heap[idx] < self.heap[parent_idx]:
            return True
        else:
            return False

    # 데이터 삽입
    def insert(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1

        # check_swap_up() 의 값이 참이라면 부모와 자리 바꾸기
        while self.check_swap_up(idx):
            parent_idx = idx // 2

            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx

        return True
    
    # 해당 노드가 자식 노드보다 작은지 비교
    def check_swap_down(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        # 자식 노드가 하나도 없을 경우
        if left_idx >= len(self.heap):
            return False        
        # 왼쪽 자식노드만 있을 경우
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] < self.heap[idx]:
                self.flag = 1
                return True
            else:
                return False
        # 자식 노드가 모두 있을 경우        
        else:
            if self.heap[left_idx] < self.heap[right_idx]:
                if self.heap[left_idx] < self.heap[idx]:
                    self.flag = 1
                    return True
                else:
                    return False
            else:
                if self.heap[right_idx] < self.heap[idx]:
                    self.flag = 2
                    return True
                else:
                    return False
                
    # 데이터 삭제
    def pop(self):
        if len(self.heap) <= 1:
            return None
        
        min = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        idx = 1

        # 0 = False, 1 = 왼쪽자식과 swap, 2 = 오른쪽자식과 swap  
        self.flag = 0

        while self.check_swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1

            if self.flag == 1:  # 왼쪽 자식값이 더 작으면 왼쪽 자식과 교체
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx
            elif self.flag == 2:    # 오른쪽 자식값이 더 작으면 오른쪽 자식과 교체
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx
        
        return min



import sys
input = sys.stdin.readline

N = int(input())

heap = MinHeap()
result = []

for i in range(N):
    x = int(input())

    if x == 0:
        if (len(heap) <= 1):
            print(0)
        else:
            print(heap.pop())
    else:
        heap.insert(x)


