from collections import deque

def solution(priorities, location):
    answer = 0   
	
    # priorities는 우선순위 리스트
    tempQueue = deque(range(0, len(priorities)))
    # 리스트를 deque로 만들어 준다.
    prioritiesque = deque(priorities)

    #location에 해당하는 배열 원소를 저장해 준다.
    value = tempQueue[location]

    isBig = False

    while value in tempQueue:
        prionum = prioritiesque.popleft()
        tempnum = tempQueue.popleft()
        for i in prioritiesque:            
            if prionum < i:
                prioritiesque.append(prionum)
                tempQueue.append(tempnum)
                isBig = True
                break
        
        if isBig == False:
            answer += 1

        isBig = False

    return answer