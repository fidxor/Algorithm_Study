from collections import deque

def solution(priorities, location):
    answer = 0   
	
    tempQueue = deque(range(0, len(priorities)))
    prioritiesque = deque(priorities)

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