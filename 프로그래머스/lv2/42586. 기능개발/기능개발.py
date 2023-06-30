from collections import deque

releaselst = []

def solution(progresses, speeds):
    answer = []

    workProgress(progresses, speeds)

    answer = releaselst.copy()

    return answer

def workProgress(progresses, speeds):
    global releaselst

    release = 0
    
    # 리스트 맨앞의 정수가 100이 되는데 걸리는 일수를 계산후 모든 리스트에 적용해서 계산.
    remainProgress = (100 - progresses[0]) // speeds[0]

    valProgress = progresses[0] + (remainProgress * speeds[0])

    if valProgress < 100:
        remainProgress += 1

    index = 0

    # 리스트 모든 원소에 계산해준다.
    for i in range(0, len(progresses)):
        progresses[i] = progresses[i] + (remainProgress * speeds[i])

    progressCopy = progresses.copy()
    speedCopy = speeds.copy()

    for i in range(0, len(progresses)):        
        if(progresses[i] >= 100):
            del progressCopy[0]
            del speedCopy[0]
            release += 1
        else:
            break

    releaselst.append(release)

    if not progressCopy:
        return

    workProgress(progressCopy, speedCopy)