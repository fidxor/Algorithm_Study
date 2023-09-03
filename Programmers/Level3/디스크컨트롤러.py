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

        if self.heap[idx][2] < self.heap[parent_idx][2]:
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
            if self.heap[left_idx][2] < self.heap[idx][2]:
                self.flag = 1
                return True
            else:
                return False
        # 자식 노드가 모두 있을 경우        
        else:
            if self.heap[left_idx][2] < self.heap[right_idx][2]:
                if self.heap[left_idx][2] < self.heap[idx][2]:
                    self.flag = 1
                    return True
                else:
                    return False
            else:
                if self.heap[right_idx][2] < self.heap[idx][2]:
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
    

def solution(jobs):
    answer = 0
    jobs.sort()
    heap = MinHeap()

    for i in jobs:
        i.append(i[0])
        
        heap.insert(i)

    jobCount = len(heap) - 1
    totalJobTime = 0
    jobInsertTime = 0
    readyTime = 0
    jobTime = 0
    beforeEndTime = 0

    while len(heap) > 1:
        job = heap.pop()
        jobInsertTime = job[0]
        readyTime = beforeEndTime - jobInsertTime
        beforeEndTime = beforeEndTime + job[1]
        if readyTime < 0:
            jobTime = job[1]
        else:
            jobTime = readyTime + job[1]        

        totalJobTime += jobTime

    return int(totalJobTime / jobCount)

print(solution([[0, 3], [10, 1]]), 2)
print(solution([[7, 8], [3, 5], [9, 6]]), 9)
print(solution([[1, 4], [7, 9], [1000, 3]]), 5)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[100, 100], [1000, 1000]]), 550)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)