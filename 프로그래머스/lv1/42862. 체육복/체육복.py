def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    lostcopy = lost.copy()

    for i in lost:
        # lost 와 reserve 에 같은 값이 있으면 제거
        if i in reserve:
            lostcopy.remove(i)
            reserve.remove(i)

    lostDuplicate = lostcopy.copy()

    for i in lostcopy:
        back = i - 1
        forward = i + 1

        if back in reserve:
            if i in lostDuplicate: lostDuplicate.remove(i)
            if back in reserve: reserve.remove(back)
        elif forward in reserve:
            if i in lostDuplicate: lostDuplicate.remove(i)
            if forward in reserve: reserve.remove(forward)

    answer = n - len(lostDuplicate)
    
    return answer